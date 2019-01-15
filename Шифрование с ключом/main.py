import sys
from PyQt5 import QtWidgets
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bEncrypt.clicked.connect(self.Encrypt)
        self.bDecrypt.clicked.connect(self.Decrypt)

    def Encrypt(self):
        len_str = self.textEdit2.toPlainText()
        k = ''
        if(len_str != ''):
            input = self.textEdit1.toPlainText()
            for elem in range((len(input))):
                k = k + chr((ord(input[elem]) + len(len_str)))
        else:
            input='Вы не ввели ключ'
        """print('Байтовая строка:',input)
        result = b64encode(input).decode()
        print('Результат шифрования:',result) """
        return self.textEdit1.setPlainText(str(k))
    
    def Decrypt(self):
        len_str = self.textEdit2.toPlainText()
        k=''
        if (len_str != ''):
            input = self.textEdit1.toPlainText()
            for elem in range((len(input))):
                k = k + chr((ord(input[elem]) - len(len_str)))
        else:
            input = 'Вы не ввели ключ'
        """print('Байтовая строка:',input)
        result = b64encode(input).decode()
        print('Результат шифрования:',result) """
        return self.textEdit1.setPlainText(str(k))
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':
    main()  
