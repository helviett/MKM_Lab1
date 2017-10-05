def initialize(self, mainForm):
    print('created', ' ', self)
    self.SaveButton.clicked.connect(lambda: self.onClick(mainForm))

def createTable(self, table):
    self.table = table
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
    filename = QFileDialog.getSaveFileName(parent, 'Save file', '', 'CSV(*.csv)')
    fout = open(list(filename)[0], 'w')
    fout.write(str(self.table))