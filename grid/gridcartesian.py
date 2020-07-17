from .grid import Grid
from PySide2.QtGui import QPen, Qt
from PySide2.QtCore import QPoint


class GridCartesian(Grid):

    def __init__(self, graphwidget, painter):
        self.graphwidget = graphwidget
        self.painter = painter
        self.width = self.graphwidget.width()
        self.height = self.graphwidget.height()
        self.origin = QPoint(self.graphwidget.width() / 2,
                             self.graphwidget.height() / 2)
        self.grid()
        self.axis()

    def grid(self):
        pen = QPen(Qt.gray, 1, Qt.DotLine)
        self.painter.setPen(pen)
        # 1 четверть
        for i in range(self.origin.x(), self.width, 20):
            self.painter.drawLine(i, 0, i, self.height / 2)
        for i in range(self.origin.y(), 0, -20):
            self.painter.drawLine(self.width / 2, i, self.width, i)
        # 2 четверть
        for i in range(self.origin.x(), 0, -20):
            self.painter.drawLine(i, 0, i, self.height / 2)
        for i in range(self.origin.y(), 0, -20):
            self.painter.drawLine(self.width / 2, i, 0, i)
        # 3 четверть
        for i in range(self.origin.x(), 0, -20):
            self.painter.drawLine(i, self.height / 2, i, self.height)
        for i in range(self.origin.y(), self.height, 20):
            self.painter.drawLine(self.width / 2, i, 0, i)
        # 4 четверть
        for i in range(self.origin.x(), self.width, 20):
            self.painter.drawLine(i, 0, i, self.height)
        for i in range(self.origin.y(), self.height, 20):
            self.painter.drawLine(self.width / 2, i, self.width, i)
