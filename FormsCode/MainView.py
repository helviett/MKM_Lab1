def initialize(self, mainForm):
    print('created', ' ', self)
    self.ChooseBtn.clicked.connect(lambda: self.onClick(mainForm))

def onClick(self, parent):
    new_window = QMainWindow(parent)
    ui = Ui_Test()
    ui.setupUi(new_window)
    new_window.setWindowTitle("New form")
    new_window.show()