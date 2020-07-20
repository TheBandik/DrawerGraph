from PySide2.QtGui import QPen, Qt
from PySide2.QtCore import QPoint

from .grid import Grid


# Отрисовка прямоугольной сетки
class GridCartesian(Grid):

    def __init__(self, graphWidget, painter):
        # Определение полученных переменных
        self.graphWidget = graphWidget
        self.painter = painter
        # Получение размеров области отрисовки
        self.width = self.graphWidget.width()
        self.height = self.graphWidget.height()
        self.origin = QPoint(self.width / 2, self.height / 2)
        self.grid()
        self.labels()
        self.labelsPX()
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

    def labels(self):
        pen = QPen(Qt.black, 1)
        self.painter.setPen(pen)
        # Отриц. ось x
        label = -2
        for i in range(self.origin.x() - 47, 0, -20):
            self.painter.drawText(i, self.height // 2 + 15, str(label))
            label -= 1
        # Пол. ось y
        label = 2
        for i in range(self.origin.y() - 36, 0, -20):
            self.painter.drawText(self.width // 2 + 9, i, str(label))
            label += 1
        # Отриц. ось y
        label = -2
        for i in range(self.origin.y() + 45, self.height, 20):
            self.painter.drawText(self.width // 2 + 5, i, str(label))
            label -= 1
