from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QPixmap, Qt

from drawer import Drawer

class GraphWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.pixmap = QPixmap(3000, 3000)
        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self.pixmap)
        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)
        Drawer(self, self.painter)
        self.painter.end()

        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.width(), self.height(), self.pixmap,
                                0, 0, self.width(), self.height())
        self.painter.end()
