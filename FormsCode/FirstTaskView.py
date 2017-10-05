def initialize(self, form):
    print('created', ' ', self)
    self.OKButton.clicked.connect(lambda: self.onClick(form))
    self.TEdit.setText('100')
    self.FEdit.setText('14')
    self.NEdit.setText('15')
    self.REdit.setText('0.33333')
    self.TcEdit.setText('20')
    self.AnalyticBox.setCheckState(3)
    self.viewModel = FirstTaskViewModel()

def onClick(self, parent):
    t = float(self.TEdit.toPlainText())
    f = float(self.FEdit.toPlainText())
    n = int(self.NEdit.toPlainText())
    r = float(self.REdit.toPlainText())
    tc = float(self.TcEdit.toPlainText())

    isAnalyticMethod = True if 2 == self.AnalyticBox.checkState() else False
    isEulerMethod = True if 2 == self.EulerBox.checkState() else False
    isRungeMethod = True if 2 == self.RungeBox.checkState() else False
    isIEulerMethod = True if 2 == self.IEulerBox.checkState() else False

    isTable = True if 2 == self.inTableCheckBox.checkState() else False
    isGraphic = True if 2 == self.GraphicCheckBox.checkState() else False

    table = self.viewModel.ConductExperiment(t, tc, r, n, f, table=isTable, graphics=isGraphic, euler=isEulerMethod, improved=isIEulerMethod, rungekutte=isRungeMethod, analitical=isAnalyticMethod)

    if (isTable):
        new_window = QMainWindow(parent)
        ui = Ui_TableForm()
        ui.setupUi(new_window)
        ui.createTable(table)
        new_window.setWindowTitle("Output table")
        new_window.show()
        