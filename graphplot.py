from PySide2.QtGui import QPen, Qt


class GraphPlot():

    def __init__(self, widget, painter):
        self.widget = widget
        self.painter = painter
        self.widget.paintEvent = self.paintEvent

    def paintEvent(self, event):
        self.painter.begin(self.widget)
        self.drawAxis()
        self.painter.end()

    def drawAxis(self):
        width = self.widget.width()
        height = self.widget.height()
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(width / 2, 0, width / 2, height)
        self.painter.drawLine(0, height / 2, width, height / 2)
