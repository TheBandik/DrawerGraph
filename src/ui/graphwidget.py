from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QPen, Qt, QBrush
from PySide2.QtCore import QPropertyAnimation, Property, QPointF

from drawer import Drawer


class GraphWidget(QWidget):

    def __init__(self, a, polar):
        super().__init__()
        self.a = a
        self.animParam = a * 10
        self.polar = polar
        self.painter = QPainter()
        self.setMinimumSize(472, 358)
        self.time = -12
        self.animation = False
        self.anim = QPropertyAnimation(self, b"animationTime")
        self.origin = QPointF(472 / 2, 358 / 2)

    def animationTime(self):
        return self.time

    def setAnimationTime(self, animationTime):
        self.time = animationTime
        self.repaint()

    def setParams(self, a, polar):
        self.a = a
        self.animParam = a * 10
        self.polar = polar
        self.repaint()

    def paintEvent(self, event):
        self.origin = QPointF(self.width() / 2, self.height() / 2)
        self.painter.begin(self)
        Drawer(self, self.painter, self.a, self.polar)
        if self.animation:
            pen = QPen(Qt.red)
            brush = QBrush(Qt.red)
            self.painter.setPen(pen)
            self.painter.setBrush(brush)
            self.painter.drawEllipse(self.findPoint(self.time), 3, 3)
        self.painter.end()

    def startAnimation(self):
        self.animation = True
        self.anim.setDuration(10000)
        self.anim.setLoopCount(-1)
        self.anim.setStartValue(-12)
        self.anim.setEndValue(12)
        self.anim.start()

    def stopAnimation(self):
        self.animation = False
        self.anim.stop()
        self.repaint()

    def findPoint(self, t):
        coord = QPointF()
        coord.setX((2 * self.animParam * t ** 2) / (1 + t ** 2))
        coord.setY((2 * self.animParam * t ** 3) / (1 + t ** 2))
        coord += self.origin
        return coord

    animationTime = Property(float, animationTime, setAnimationTime)
