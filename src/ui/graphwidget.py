from math import ceil, floor

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QPen, Qt, QBrush
from PySide2.QtCore import QPropertyAnimation, Property, QPointF

from drawer import Drawer


# Область отрисовки графика
class GraphWidget(QWidget):

    def __init__(self, a, polar):
        super().__init__()
        # Определение полученных переменных
        self.a = a
        self.polar = polar
        # Параметр a с коэффициентом для анимации
        self.animParam = a * 10
        # Переменные для анимации
        self.time = -12
        self.anim = QPropertyAnimation(self, b"animationTime")
        self.painter = QPainter()
        self.animation = False
        # Параметр области отрисовки
        self.setMinimumSize(472, 360)

    def animationTime(self):
        return self.time

    def setAnimationTime(self, animationTime):
        self.time = animationTime
        self.repaint()

    # Установка новых параметров
    def setParams(self, a, polar):
        # Определение полученных переменных
        self.a = a
        self.polar = polar
        # Параметр a с коэффициентом для анимации
        self.animParam = a * 10
        # Перезапуск анимации для новых параметров
        if self.animation:
            self.anim.stop()
            self.startAnimation()
        self.repaint()

    # Ивент отрисовки
    def paintEvent(self, event):
        # Центр области отрисовки
        self.origin = QPointF(self.width() / 2, self.height() / 2)
        # Рисование
        self.painter.begin(self)
        Drawer(self, self.painter, self.a, self.polar)
        # Если включена анимация, то рисуется красный круг
        if self.animation:
            pen = QPen(Qt.red)
            brush = QBrush(Qt.red)
            self.painter.setPen(pen)
            self.painter.setBrush(brush)
            if self.time % 1 != 0.00:
                self.painter.drawEllipse(self.findPoint(self.time), 3, 3)
        self.painter.end()

    # Запуск анимации
    def startAnimation(self):
        self.animation = True
        # Время анимации
        self.anim.setDuration(10000)
        # Зацикливание
        self.anim.setLoopCount(-1)
        # Начальное значение времени анимации
        self.anim.setStartValue(floor(self.height() / -35.8 / self.a) - .5)
        # Конечное значение времени анимации
        self.anim.setEndValue(ceil(self.height() / 35.8 / self.a) + .5)
        # Старт
        self.anim.start()

    # Остановка анимации
    def stopAnimation(self):
        self.animation = False
        self.anim.stop()
        self.repaint()

    # Нахождение точки для анимации
    def findPoint(self, t):
        coord = QPointF()
        # Параметрические формулы кривой
        coord.setX((2 * self.animParam * t ** 2) / (1 + t ** 2))
        coord.setY((2 * self.animParam * t ** 3) / (1 + t ** 2))
        # Смещение относительно центра координат
        coord += self.origin
        return coord

    # Ивент масштабирования
    def resizeEvent(self, event):
        # Установка новых начального и конечного значений времени анимации
        if self.animation:
            self.anim.pause()
            self.anim.setStartValue(floor(self.height() / -35.8 / self.a) - .5)
            self.anim.setEndValue(ceil(self.height() / 35.8 / self.a) + .5)
            self.anim.resume()

    # Определение нового свойства подсчета времени анимации для виджета
    animationTime = Property(float, animationTime, setAnimationTime)
