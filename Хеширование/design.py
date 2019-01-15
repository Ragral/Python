# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.bEncrypt.setGeometry(QtCore.QRect(60, 140, 211, 31))
        self.bEncrypt.setObjectName("bEncrypt")
     #   self.bDecrypt = QtWidgets.QPushButton(self.centralwidget)
    #    self.bDecrypt.setGeometry(QtCore.QRect(170, 140, 151, 31))
    #    self.bDecrypt.setObjectName("bDecrypt")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 311, 121))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bEncrypt.setText(_translate("MainWindow", "Зашифровать"))
     #   self.bDecrypt.setText(_translate("MainWindow", "Расшифровать"))

