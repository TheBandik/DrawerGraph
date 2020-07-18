from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter

from drawer import Drawer


class GraphWidget(QWidget):

    def __init__(self, a):
        super().__init__()
        self.a = a
        self.painter = QPainter()

    def setParams(self, a):
        self.a = a
        self.repaint()

    def paintEvent(self, event):
        self.painter.begin(self)
        Drawer(self, self.painter, self.a)
        self.painter.end()
