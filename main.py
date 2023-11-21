import sys
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication

class Coff(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffe_table')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(630, 430)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Coff()
    c.show()
    sys.exit(app.exec_())
