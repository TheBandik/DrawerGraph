from PySide2.QtGui import QPen, Qt
from PySide2.QtCore import QPoint, QLineF

from .grid import Grid


class GridPolar(Grid):

    def __init__(self, graphwidget, painter):
        self.graphwidget = graphwidget
        self.painter = painter
        self.width = self.graphwidget.width()
        self.height = self.graphwidget.height()
        self.origin = QPoint(self.graphwidget.width() / 2,
                             self.graphwidget.height() / 2)
        self.line = QLineF()
        self.line.setP1(self.origin)
        self.line.setLength(self.width // 3)
        self.grid()
        self.labelsPX()
        self.addAxis()
        self.axis()
        self.labels()

    def grid(self):
        pen = QPen(Qt.red, 1, Qt.DotLine)
        self.painter.setPen(pen)
        n = self.width // 3 if self.width > self.height else self.height // 3
        for i in range(0, n, 20):
            self.painter.drawEllipse(self.origin, i, i)

    def addAxis(self):
        pen = QPen(Qt.gray, 1, Qt.DotLine)
        self.painter.setPen(pen)
        for i in range(30, 360, 30):
            if i != 90 and i != 180 and i != 270:
                self.line.setAngle(i)
                self.painter.drawLine(self.line)

    def labels(self):
        pen = QPen(Qt.black, 1)
        self.painter.setPen(pen)
        self.line.setLength(self.width // 6)
        point = QPoint()
        for i in range(30, 360, 30):
            if i != 90 and i != 180 and i != 270:
                self.line.setAngle(i)
                point = self.line.p2()
                point.setX(point.x() - 5)
                point.setY(point.y() + 5)
                self.painter.drawText(point, str(i))
