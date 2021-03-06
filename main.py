import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 450)
        self.setWindowTitle('Circles')
        self.btn = QPushButton('Push', self)
        self.btn.move(210, 350)


class MyWidget(UI):
    def __init__(self):
        super().__init__()
        UI()
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        col1 = randint(0, 255)
        col2 = randint(0, 255)
        col3 = randint(0, 255)
        qp.setBrush(QColor(col1, col2, col3))
        r = randint(1, 240)
        qp.drawEllipse(100, 100, r, r)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
