from .grid import Grid
from PySide2.QtGui import QPen, Qt


class GridCartesian(Grid):

    def __init__(self, graphwidget, painter):
        self.graphwidget = graphwidget
        self.painter = painter
        self.width = self.graphwidget.width()
        self.height = self.graphwidget.height()
        self.grid()
        self.axis()

    def grid(self):
        pen = QPen(Qt.gray, 1, Qt.DotLine)
        self.painter.setPen(pen)
        for i in range(20, self.width, 20):
            self.painter.drawLine(i, 0, i, self.height)
        for i in range(20, self.height, 20):
            self.painter.drawLine(0, i, self.width, i)
