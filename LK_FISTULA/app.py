from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForms(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=3, max=20)])
    remember = BooleanField('Запомнить меня')

class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('Почта', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=3, max=20)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember = form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1>Неправильный логин или пароль</h1>'

    return render_template('login.html', form = form)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        directory = os.path.dirname(__file__) + '\\user_simple\\' + form.email.data
        os.makedirs(directory)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form = form)

@app.route('/dashboard')
@login_required
def dashboard():
    directory = os.path.dirname(__file__) + '\\user_simple\\' + current_user.username
    simple_user = os.listdir(directory)
    return render_template('dashboard.html', name = current_user.username, simple = simple_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/download/<path:filename>')
@login_required
def download_file(filename):
	directory=os.path.dirname(__file__) +'\\user_simple\\' + current_user.username
	return send_from_directory(directory,filename, as_attachment=True)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
