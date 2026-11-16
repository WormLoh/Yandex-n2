import sys
import random
from PyQt6 import uic
from PyQt6.QtCore import QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.trigger_paint)
        self.do_paint = False

    def trigger_paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.do_paint = False

    def draw_flag(self, qp):
        center = QPointF(360, 240)
        radius = random.randint(5, 200)
        rect = QRectF(center.x() - radius, center.y() - radius, 2*radius, 2*radius)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())