import sys
from PyQt5 import QtWidgets
import design
import rsa
from base64 import b64encode, b64decode

(pubkey, privkey) = rsa.newkeys(512)

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bEncrypt.clicked.connect(self.Encrypt)
        self.bDecrypt.clicked.connect(self.Decrypt)

    def Encrypt(self):
        input = self.textEdit.toPlainText()
        input = rsa.encrypt(bytes(input, 'utf-8'), pubkey)
        result = b64encode(input).decode()    
        return self.textEdit.setPlainText(str(result))
    
    def Decrypt(self):
        input = self.textEdit.toPlainText()
        input = b64decode(input)
        result = rsa.decrypt(input, privkey).decode('utf-8')
        return self.textEdit.setPlainText(str(result)) 
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':
    main()  
