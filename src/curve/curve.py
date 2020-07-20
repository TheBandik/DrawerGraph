from math import floor, ceil

from PySide2.QtCore import QPointF, Qt
from PySide2.QtGui import QPen


class Curve():

    def __init__(self, graphwidget, painter, a):
        self.graphwidget = graphwidget
        self.painter = painter
        self.a = a * 10
        self.lastCoord = QPointF()
        self.first = True
        self.origin = QPointF(self.graphwidget.width() / 2,
                              self.graphwidget.height() / 2)
        self.draw()

    def draw(self):
        pen = QPen(Qt.blue, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        fi = floor(self.graphwidget.height() / -35.8 / (self.a / 10))
        end = ceil(self.graphwidget.height() / 35.8 / (self.a / 10))
        while fi <= end:
            point = QPointF()
            point = self.findPoint(fi)
            if self.first:
                self.first = False
            else:
                self.painter.drawLine(point, self.lastCoord)
            self.lastCoord = point
            fi += 0.01

    def findPoint(self, t):
        coord = QPointF()
        coord.setX((2 * self.a * t ** 2) / (1 + t ** 2))
        coord.setY((2 * self.a * t ** 3) / (1 + t ** 2))
        coord += self.origin
        return coord
