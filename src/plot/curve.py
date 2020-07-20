from math import floor, ceil

from PySide2.QtCore import QPointF, Qt
from PySide2.QtGui import QPen


# Отрисовка кривой
class Curve():

    def __init__(self, graphWidget, painter, a):
        # Определение полученных переменных
        self.graphWidget = graphWidget
        self.painter = painter
        self.a = a * 10
        # Последняя полученная точка
        self.lastCoord = QPointF()
        # Первая точка
        self.first = True
        # Центр координат
        self.origin = QPointF(self.graphWidget.width() / 2,
                              self.graphWidget.height() / 2)
        # Рисование кривой
        self.draw()

    # Рисование кривой
    def draw(self):
        pen = QPen(Qt.blue, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        # Начальная точка
        fi = floor(self.graphWidget.height() / -35.8 / (self.a / 10) - .5)
        # Конечная точка
        end = ceil(self.graphWidget.height() / 35.8 / (self.a / 10) + .5)
        # Отрисовка всех точек
        while fi <= end:
            # Нахождение точки
            point = QPointF()
            point = self.findPoint(fi)
            # Если точка первая, то она не рисуется
            if self.first:
                self.first = False
            else:
                self.painter.drawLine(point, self.lastCoord)
            # Запись прошлой точки
            self.lastCoord = point
            # Следующая итерация
            fi += 0.01

    # Нахождение точки
    def findPoint(self, t):
        coord = QPointF()
        # Параметрические формулы кривой
        coord.setX((2 * self.a * t ** 2) / (1 + t ** 2))
        coord.setY((2 * self.a * t ** 3) / (1 + t ** 2))
        # Смещение относительно центра координат
        coord += self.origin
        return coord
