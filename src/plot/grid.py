from PySide2.QtGui import QPen, Qt


class Grid():

    def axis(self):
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(self.width / 2, 0, self.width / 2, self.height)
        self.painter.drawLine(0, self.height / 2, self.width, self.height / 2)

    def labelsPX(self):
        pen = QPen(Qt.black, 1)
        self.painter.setPen(pen)
        label = 2
        # Пол. ось x
        for i in range(self.origin.x() + 37, self.width, 20):
            self.painter.drawText(i, self.height // 2 + 15, str(label))
            label += 1
