from PySide2.QtGui import QPen, Qt
from PySide2.QtCore import QPoint, QLineF

from .grid import Grid


# Отрисовка полярной сетки
class GridPolar(Grid):

    def __init__(self, graphWidget, painter):
        # Определение полученных переменных
        self.graphWidget = graphWidget
        self.painter = painter
        # Получение размеров области отрисовки
        self.width = self.graphWidget.width()
        self.height = self.graphWidget.height()
        # Центр координат
        self.origin = QPoint(self.width / 2,
                             self.height / 2)
        # Линия координат
        self.line = QLineF()
        self.line.setP1(self.origin)
        self.line.setLength(self.width // 3)
        # Отрисовка сетки
        self.grid()
        # Отрисовка цифр на оси X
        self.labelsPX()
        # Отрисовка линий координат
        self.addAxis()
        # Отрисовка осей координат
        self.axis()
        # Отрисовка градусов
        self.labels()

    # Отрисовка сетки
    def grid(self):
        pen = QPen(Qt.red, 1, Qt.DotLine)
        self.painter.setPen(pen)
        # Коэффициент масштабирования
        n = self.width // 3 if self.width > self.height else self.height // 3
        # Отрисовка эллипсов
        for i in range(0, n, 20):
            self.painter.drawEllipse(self.origin, i, i)

    # Отрисовка линий координат
    def addAxis(self):
        pen = QPen(Qt.gray, 1, Qt.DotLine)
        self.painter.setPen(pen)
        # Отрисовка линий с шагом в 30 градусов
        for i in range(30, 360, 30):
            if i != 90 and i != 180 and i != 270:
                self.line.setAngle(i)
                self.painter.drawLine(self.line)

    # Отрисовка градусов
    def labels(self):
        pen = QPen(Qt.black, 1)
        self.painter.setPen(pen)
        self.line.setLength(self.width // 6)
        point = QPoint()
        # Определение линий с шагом в 30 градусов
        for i in range(30, 360, 30):
            if i != 90 and i != 180 and i != 270:
                self.line.setAngle(i)
                point = self.line.p2()
                # Нахождение центра определенной линии
                point.setX(point.x() - 5)
                point.setY(point.y() + 5)
                # Отрисовка градуса
                self.painter.drawText(point, str(i))
