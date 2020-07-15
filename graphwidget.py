from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import QSize

from graphplot import GraphPlot


class GraphWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(200, 200))
        painter = QPainter()
        GraphPlot(self, painter)
