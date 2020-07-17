from grid.gridcartesian import GridCartesian
from curve.curve import Curve


class Drawer():

    def __init__(self, graphwidget, painter, param):
        self.graphwidget = graphwidget
        self.painter = painter
        self.param = param
        self.drawGraph()

    def drawGraph(self):
        GridCartesian(self.graphwidget, self.painter)
        Curve(self.graphwidget, self.painter, self.param)
