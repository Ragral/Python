# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.bEncrypt.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.bEncrypt.setObjectName("bEncrypt")
        self.bDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.bDecrypt.setGeometry(QtCore.QRect(170, 180, 151, 31))
        self.bDecrypt.setObjectName("bDecrypt")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(10, 10, 311, 121))
        self.textEdit1.setObjectName("textEdit")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(170, 140, 151, 31))
        self.textEdit2.setObjectName("key")
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
        self.bDecrypt.setText(_translate("MainWindow", "Расшифровать"))

