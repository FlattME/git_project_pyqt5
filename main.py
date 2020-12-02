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

        self.btn.clicked.connect(self.edit)

    def edit(self):
        self.d = editWindow()
        self.d.show()
        self.close()


class editWindow(QMainWindow):
    def __init__(self):
        super(editWindow, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")

        self.cur = self.con.cursor()

        self.edit_btn.clicked.connect(self.edit_def)
        self.add_btn.clicked.connect(self.add_def)

    def edit_def(self):
        self.cur.execute(
            f"UPDATE COFFEE "
            f"SET название_сорта='{self.lineEdit_11.text()}', степень_обжарки='{self.lineEdit_7.text()}', молотый/в_зернах='{self.lineEdit_8.text()}',описание_вкуса='{self.lineEdit_10.text()}', цена={self.lineEdit_9.text()}, объем_упаковки={self.lineEdit_13.text()}"
            f" WHERE ID = {self.lineEdit_12.text()}")
        self.con.commit()

    def add_def(self):
        self.cur.execute(
            f"INSERT INTO COFFEE(ID,название_сорта,степень_обжарки,молотый/в_зернах,описание_вкуса,цена,объем_упаковки)"
            f" VALUES({self.lineEdit_16.text()},{self.lineEdit_19.text()},{self.lineEdit_15.text()},{self.lineEdit_17.text()},{self.lineEdit_14.text()},{self.lineEdit_18.text()})")
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

