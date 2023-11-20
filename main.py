from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
import random
import sys


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        diameter = random.randint(100, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(150 - diameter // 2, 230 - diameter // 2, diameter, diameter)

        diameter2 = random.randint(100, 200)
        qp.drawEllipse(450 - diameter2 // 2, 230 - diameter2 // 2, diameter2, diameter2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    f.show()
    sys.exit(app.exec_())
