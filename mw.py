# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/maximpashkovsky/Desktop/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.le_a = QtWidgets.QLineEdit(self.centralwidget)
        self.le_a.setGeometry(QtCore.QRect(10, 10, 113, 22))
        self.le_a.setObjectName("le_a")
        self.le_b = QtWidgets.QLineEdit(self.centralwidget)
        self.le_b.setGeometry(QtCore.QRect(170, 10, 113, 22))
        self.le_b.setObjectName("le_b")
        self.le_result = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result.setGeometry(QtCore.QRect(330, 10, 113, 22))
        self.le_result.setObjectName("le_result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 16, 16))
        self.label_4.setObjectName("label_4")
        self.le_a_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_a_2.setGeometry(QtCore.QRect(10, 60, 113, 22))
        self.le_a_2.setObjectName("le_a_2")
        self.le_result_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result_2.setGeometry(QtCore.QRect(330, 60, 113, 22))
        self.le_result_2.setObjectName("le_result_2")
        self.le_b_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_b_2.setGeometry(QtCore.QRect(170, 60, 113, 22))
        self.le_b_2.setObjectName("le_b_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 110, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 110, 16, 16))
        self.label_6.setObjectName("label_6")
        self.le_a_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_a_3.setGeometry(QtCore.QRect(10, 110, 113, 22))
        self.le_a_3.setObjectName("le_a_3")
        self.le_result_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result_3.setGeometry(QtCore.QRect(330, 110, 113, 22))
        self.le_result_3.setObjectName("le_result_3")
        self.le_b_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_b_3.setGeometry(QtCore.QRect(170, 110, 113, 22))
        self.le_b_3.setObjectName("le_b_3")
        self.le_a_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_a_4.setGeometry(QtCore.QRect(10, 170, 113, 22))
        self.le_a_4.setObjectName("le_a_4")
        self.le_b_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_b_4.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.le_b_4.setObjectName("le_b_4")

        self.le_a_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_a_5.setGeometry(QtCore.QRect(10, 200, 133, 22))
        self.le_a_5.setObjectName("le_b_4")

        self.le_b_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_b_5.setGeometry(QtCore.QRect(170, 200, 133, 22))
        self.le_b_5.setObjectName("le_b_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "="))
        self.label_3.setText(_translate("MainWindow", "-"))
        self.label_4.setText(_translate("MainWindow", "="))
        self.label_5.setText(_translate("MainWindow", "%"))
        self.label_6.setText(_translate("MainWindow", "="))
