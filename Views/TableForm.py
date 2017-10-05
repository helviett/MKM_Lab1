# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TableForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableForm(object):
    def setupUi(self, TableForm):
        TableForm.setObjectName("TableForm")
        TableForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TableForm)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        TableForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TableForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableForm)
        self.statusbar.setObjectName("statusbar")
        TableForm.setStatusBar(self.statusbar)

        self.retranslateUi(TableForm)
        QtCore.QMetaObject.connectSlotsByName(TableForm)

    def retranslateUi(self, TableForm):
        _translate = QtCore.QCoreApplication.translate
        TableForm.setWindowTitle(_translate("TableForm", "MainWindow"))

