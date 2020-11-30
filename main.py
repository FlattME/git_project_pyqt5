import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import random


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('SQL2.ui', self)
        self.flag = False

        self.btn.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        c = random.randint(10, 100)
        self.qp.drawEllipse(*[random.randint(10, 700), random.randint(10, 500)], c, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

