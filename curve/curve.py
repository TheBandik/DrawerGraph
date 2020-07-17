from PySide2.QtCore import QPointF, Qt
from PySide2.QtGui import QPen


class Curve():

    def __init__(self, graphwidget, painter, param):
        self.graphwidget = graphwidget
        self.painter = painter
        self.param = param * 10
        self.first = True
        self.lastCoord = QPointF()
        self.origin = QPointF(self.graphwidget.width() / 2,
                              self.graphwidget.height() / 2)
        self.draw()

    def draw(self):
        pen = QPen(Qt.red, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        fi = -1000
        while fi <= 1000:
            point = QPointF()
            point = self.findPoint(fi)
            if self.first:
                self.first = False
            else:
                self.painter.drawLine(point, self.lastCoord)

            self.lastCoord = point
            fi += 0.1

    def findPoint(self, t):
        coord = QPointF()
        coord.setX((2 * self.param * t ** 2) / (1 + t ** 2))
        coord.setY((2 * self.param * t ** 3) / (1 + t ** 2))
        coord += self.origin
        return coord
