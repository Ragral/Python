import sys
from PyQt5 import QtWidgets
import design
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

cipher = Fernet(Fernet.generate_key())


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bEncrypt.clicked.connect(self.Encrypt)
        self.bDecrypt.clicked.connect(self.Decrypt)

    def Encrypt(self):
        input = self.textEdit.toPlainText()
        input = cipher.encrypt(bytes(input, 'utf-8'))
        print('Байтовая строка:',input)
        result = b64encode(input).decode()
        print('Результат шифрования:',result)
        return self.textEdit.setPlainText(str(result))
    
    def Decrypt(self):
        input = self.textEdit.toPlainText()
        input = b64decode(input)
        print('Байтовая строка:',input)
        result = cipher.decrypt(input).decode('utf-8')
        print('Результат шифрования:',result)
        return self.textEdit.setPlainText(str(result)) 
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':
    main()  
