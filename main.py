import sys
import random
from PyQt6.QtCore import QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.setWindowTitle('Круги')

        btn = QPushButton('Круг', self)
        btn.resize(80, 50)
        btn.move(250, 400)
        btn.clicked.connect(self.trigger_paint)

        self.do_paint = False

    def trigger_paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_paint = False

    def draw_circle(self, qp):
        center = QPointF(300, 220)
        radius = random.randint(5, 200)
        rect = QRectF(center.x() - radius, center.y() - radius, 2*radius, 2*radius)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())