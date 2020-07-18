from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter

from drawer import Drawer


class GraphWidget(QWidget):

    def __init__(self, param):
        super().__init__()
        self.painter = QPainter()
        self.param = param

    def paintEvent(self, event):
        self.painter.begin(self)
        Drawer(self, self.painter, self.param)
        self.painter.end()
