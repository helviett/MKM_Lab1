def initialize(self, form):
    print('created', ' ', self)
    self.OKButton.clicked.connect(lambda: self.onClick(form))
    self.TEdit.setText('0')
    self.FEdit.setText('0')
    self.NEdit.setText('0')
    self.REdit.setText('0')
    self.AnalyticBox.setCheckState(3)

def onClick(self, parent):
    t = self.TEdit.toPlainText()
    f = self.FEdit.toPlainText()
    n = self.NEdit.toPlainText()
    r = self.REdit.toPlainText()
    isAnalyticMethod = self.AnalyticBox.checkState()
    isEulerMethod = self.EulerBox.checkState()
    isRungeMethod = self.RungeBox.checkState()
    isIEulerMethod = self.IEulerBox.checkState()