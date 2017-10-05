from PyQt5.QtWidgets import *
from GenCode.Test import *
from GenCode.FirstTaskView import *
from GenCode.TableForm import *
from ViewModels.FirstTaskViewModel  import *
from ViewModels.__pycache__ import *
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(524, 283)
        self.centralwidget = QtWidgets.QWidget(MainView)
        self.centralwidget.setObjectName("centralwidget")
        self.TaskLabel = QtWidgets.QLabel(self.centralwidget)
        self.TaskLabel.setGeometry(QtCore.QRect(60, 60, 111, 16))
        self.TaskLabel.setObjectName("TaskLabel")
        self.TaskComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TaskComboBox.setGeometry(QtCore.QRect(210, 60, 111, 22))
        self.TaskComboBox.setObjectName("TaskComboBox")
        self.TaskComboBox.addItem("")
        self.ChooseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseBtn.setGeometry(QtCore.QRect(350, 60, 91, 22))
        self.ChooseBtn.setObjectName("ChooseBtn")
        MainView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 19))
        self.menubar.setObjectName("menubar")
        MainView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainView)
        self.statusbar.setObjectName("statusbar")
        MainView.setStatusBar(self.statusbar)

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

        self.initialize(MainView)

    def retranslateUi(self, MainView):
        _translate = QtCore.QCoreApplication.translate
        MainView.setWindowTitle(_translate("MainView", "MainWindow"))
        self.TaskLabel.setText(_translate("MainView", "Выбор задания"))
        self.TaskComboBox.setItemText(0, _translate("MainView", "Задание N1"))
        self.ChooseBtn.setText(_translate("MainView", "Выбрать"))

    def initialize(self, mainForm):
        print('created', ' ', self)
        self.ChooseBtn.clicked.connect(lambda: self.onClick(mainForm))
    
    def onClick(self, parent):
        new_window = QMainWindow(parent)
        ui = Ui_FirstTaskView()
        ui.setupUi(new_window)
        new_window.setWindowTitle("New form")
        new_window.show()