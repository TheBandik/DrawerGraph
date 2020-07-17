from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, Qt

from drawer import Drawer


class GraphWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)
        Drawer(self, self.painter)
        self.painter.end()
