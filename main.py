from random import randrange
import sys
from PyQt5 import uic
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QWidget, QInputDialog, QErrorMessage, QApplication, QMainWindow
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QPainter


class Ellipses(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ellipses = []
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.new_ellipse)

    def new_ellipse(self):
        x, y, r = randrange(0, 1000), randrange(0, 800), randrange(1, 200)
        self.ellipses.append((x, y, r))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for el in self.ellipses:
            qp.drawEllipse(el[0], el[1], el[2], el[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipses()
    ex.show()
    sys.exit(app.exec_())