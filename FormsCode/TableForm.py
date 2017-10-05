def initialize(self, mainForm):
    print('created', ' ', self)

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