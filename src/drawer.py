from grid.gridcartesian import GridCartesian
from grid.gridpolar import GridPolar
from curve.curve import Curve


class Drawer():

    def __init__(self, graphwidget, painter, a, polar):
        self.graphwidget = graphwidget
        self.painter = painter
        self.a = a
        self.polar = polar
        self.drawGraph()

    def drawGraph(self):
        if self.polar:
            GridPolar(self.graphwidget, self.painter)
        else:
            GridCartesian(self.graphwidget, self.painter)
        Curve(self.graphwidget, self.painter, self.a)