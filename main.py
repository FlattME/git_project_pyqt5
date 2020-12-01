import sys

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QPushButton, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")

        self.cur = self.con.cursor()
        self.result = self.cur.execute("SELECT * FROM COFFEE").fetchall()


        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

