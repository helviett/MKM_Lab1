# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/firsttaskview.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstTaskView(object):
    def setupUi(self, FirstTaskView):
        FirstTaskView.setObjectName("FirstTaskView")
        FirstTaskView.resize(501, 319)
        self.centralwidget = QtWidgets.QWidget(FirstTaskView)
        self.centralwidget.setObjectName("centralwidget")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(190, 240, 93, 28))
        self.OKButton.setObjectName("OKButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 411, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Tlabel = QtWidgets.QLabel(self.layoutWidget)
        self.Tlabel.setObjectName("Tlabel")
        self.gridLayout.addWidget(self.Tlabel, 0, 0, 1, 1)
        self.Flabel = QtWidgets.QLabel(self.layoutWidget)
        self.Flabel.setObjectName("Flabel")
        self.gridLayout.addWidget(self.Flabel, 1, 0, 1, 1)
        self.TEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.TEdit.setObjectName("TEdit")
        self.gridLayout.addWidget(self.TEdit, 0, 1, 1, 1)
        self.REdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.REdit.setObjectName("REdit")
        self.gridLayout.addWidget(self.REdit, 0, 4, 1, 1)
        self.FEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.FEdit.setObjectName("FEdit")
        self.gridLayout.addWidget(self.FEdit, 1, 1, 1, 1)
        self.Nlabel = QtWidgets.QLabel(self.layoutWidget)
        self.Nlabel.setObjectName("Nlabel")
        self.gridLayout.addWidget(self.Nlabel, 1, 2, 1, 2)
        self.Rlabel = QtWidgets.QLabel(self.layoutWidget)
        self.Rlabel.setObjectName("Rlabel")
        self.gridLayout.addWidget(self.Rlabel, 0, 2, 1, 2)
        self.NEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.NEdit.setObjectName("NEdit")
        self.gridLayout.addWidget(self.NEdit, 1, 4, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 110, 412, 49))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AnalyticBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.AnalyticBox.setObjectName("AnalyticBox")
        self.gridLayout_2.addWidget(self.AnalyticBox, 0, 0, 1, 1)
        self.EulerBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.EulerBox.setObjectName("EulerBox")
        self.gridLayout_2.addWidget(self.EulerBox, 0, 1, 1, 1)
        self.RungeBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.RungeBox.setObjectName("RungeBox")
        self.gridLayout_2.addWidget(self.RungeBox, 1, 0, 1, 1)
        self.IEulerBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.IEulerBox.setObjectName("IEulerBox")
        self.gridLayout_2.addWidget(self.IEulerBox, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 190, 341, 22))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.inTableCheckBox = QtWidgets.QCheckBox(self.widget)
        self.inTableCheckBox.setObjectName("inTableCheckBox")
        self.gridLayout_3.addWidget(self.inTableCheckBox, 0, 0, 1, 1)
        self.GraphicCheckBox = QtWidgets.QCheckBox(self.widget)
        self.GraphicCheckBox.setObjectName("GraphicCheckBox")
        self.gridLayout_3.addWidget(self.GraphicCheckBox, 0, 1, 1, 1)
        FirstTaskView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FirstTaskView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 26))
        self.menubar.setObjectName("menubar")
        FirstTaskView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FirstTaskView)
        self.statusbar.setObjectName("statusbar")
        FirstTaskView.setStatusBar(self.statusbar)

        self.retranslateUi(FirstTaskView)
        QtCore.QMetaObject.connectSlotsByName(FirstTaskView)

    def retranslateUi(self, FirstTaskView):
        _translate = QtCore.QCoreApplication.translate
        FirstTaskView.setWindowTitle(_translate("FirstTaskView", "MainWindow"))
        self.OKButton.setText(_translate("FirstTaskView", "Ok"))
        self.Tlabel.setText(_translate("FirstTaskView", "T0 = "))
        self.Flabel.setText(_translate("FirstTaskView", "f = "))
        self.Nlabel.setText(_translate("FirstTaskView", "n = "))
        self.Rlabel.setText(_translate("FirstTaskView", "r = "))
        self.AnalyticBox.setText(_translate("FirstTaskView", "Аналитический метод"))
        self.EulerBox.setText(_translate("FirstTaskView", "Метод Эйлера"))
        self.RungeBox.setText(_translate("FirstTaskView", "Метод Рунге-Кутты"))
        self.IEulerBox.setText(_translate("FirstTaskView", "Усовершенствованный метод Эйлера"))
        self.inTableCheckBox.setText(_translate("FirstTaskView", "Вывсти в таблицу"))
        self.GraphicCheckBox.setText(_translate("FirstTaskView", "Вывести график"))
