#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from GenCode.MainView import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainView = QMainWindow()
    ui = Ui_MainView()
    ui.setupUi(mainView)

    mainView.show()

    sys.exit(app.exec_())