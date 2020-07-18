from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter

from drawer import Drawer


class GraphWidget(QWidget):

    def __init__(self, a, polar):
        super().__init__()
        self.a = a
        self.polar = polar
        self.painter = QPainter()
        self.setMinimumSize(472, 358)

    def setParams(self, a, polar):
        self.a = a
        self.polar = polar
        self.repaint()

    def paintEvent(self, event):
        self.painter.begin(self)
        Drawer(self, self.painter, self.a, self.polar)
        self.painter.end()
