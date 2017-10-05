from PyQt5.QtWidgets import *
from GenCode.FirstTaskView import *
from GenCode.MainView import *
from GenCode.Test import *
from ViewModels.FirstTaskViewModel  import *
from ViewModels.__pycache__ import *
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
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(350, 520, 93, 28))
        self.SaveButton.setObjectName("SaveButton")
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

        self.initialize(TableForm)

    def retranslateUi(self, TableForm):
        _translate = QtCore.QCoreApplication.translate
        TableForm.setWindowTitle(_translate("TableForm", "MainWindow"))
        self.SaveButton.setText(_translate("TableForm", "Сохранить"))

    def initialize(self, mainForm):
        print('created', ' ', self)
        self.SaveButton.clicked.connect(lambda: self.onClick(mainForm))
    
    def createTable(self, table):
        n = table.ColCount()
        m = table.RowCount()
        self.tableWidget.setColumnCount(table.ColCount())
        self.tableWidget.setRowCount(table.RowCount())
        self.tableWidget.setHorizontalHeaderLabels(table.Cols())
        w = 0
        for i in range(m):
            for j in range(n):
                self.tableWidget.setItem(i, j, QTableWidgetItem(table[i][j]))
    
        self.tableWidget.resizeColumnsToContents()
    
    def onClick(self, parent):
        filename = QFileDialog.getSaveFileName(parent, 'Save file', '/home')
        fout = open(list(filename)[0], 'w')
        fout.write('Hellow world')