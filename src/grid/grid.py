from PySide2.QtGui import QPen, Qt


class Grid():

    def axis(self):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(self.width / 2, 0, self.width / 2, self.height)
        self.painter.drawLine(0, self.height / 2, self.width, self.height / 2)
