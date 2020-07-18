from grid.gridcartesian import GridCartesian
from curve.curve import Curve


class Drawer():

    def __init__(self, graphwidget, painter, a):
        self.graphwidget = graphwidget
        self.painter = painter
        self.a = a
        self.drawGraph()

    def drawGraph(self):
        GridCartesian(self.graphwidget, self.painter)
        Curve(self.graphwidget, self.painter, self.a)
