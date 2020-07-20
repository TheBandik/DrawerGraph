from plot.gridcartesian import GridCartesian
from plot.gridpolar import GridPolar
from plot.curve import Curve


# Вызывает методы рисования
class Drawer():

    def __init__(self, graphWidget, painter, a, polar):
        # Определение полученных переменных
        self.graphWidget = graphWidget
        self.painter = painter
        self.a = a
        self.polar = polar
        # Запуск рисования
        self.drawPlot()

    def drawPlot(self):
        # Рисование сетки
        if self.polar:
            # Полярная
            GridPolar(self.graphWidget, self.painter)
        else:
            # Прямоугольная
            GridCartesian(self.graphWidget, self.painter)
        # Рисование кривой
        Curve(self.graphWidget, self.painter, self.a)
