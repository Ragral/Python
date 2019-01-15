import sys
from PyQt5 import QtWidgets
import design
import hashlib
from base64 import b64encode, b64decode


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bEncrypt.clicked.connect(self.Encrypt)

    def Encrypt(self):
        input = self.textEdit.toPlainText()
        input = hashlib.sha1(bytes(input, 'utf-8')).hexdigest()
       # result = b64encode(input).decode()
        return self.textEdit.setPlainText(str(input))
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':
    main()  
