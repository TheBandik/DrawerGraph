from PySide2.QtWidgets import (
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from PySide2.QtCore import QSize

from .graphwidget import GraphWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.CreateUi()
        self.show()

    def CreateUi(self):
        self.setWindowTitle("Graph")
        self.resize(640, 380)
        # TODO иконка
        # icon_main_window = QIcon("icon_main_window.png")
        # self.setWindowIcon(icon_main_window)

        # Макеты
        self.mainLayout = QHBoxLayout()
        self.panelLayout = QVBoxLayout()
        self.groupBoxParameterLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        # Виджет
        self.graphWidget = GraphWidget()
        # Панель
        self.panel = QWidget()
        self.panel.setMinimumSize(QSize(200, 0))
        self.panel.setMaximumSize(QSize(200, 1000000))
        self.panel.setLayout(self.panelLayout)
        # Параметр
        self.groupBoxParameter = QGroupBox("Parameter", self.panel)
        self.groupBoxParameter.setLayout(self.groupBoxParameterLayout)
        self.doubleSpinBox = QDoubleSpinBox(self.groupBoxParameter)
        # Кнопки
        self.updateButton = QPushButton("Update", self.panel)
        self.systemButton = QPushButton("System", self.panel)
        # Добавление виджетов в макет
        self.mainLayout.addWidget(self.graphWidget)
        self.mainLayout.addWidget(self.panel)
        self.groupBoxParameterLayout.addWidget(self.doubleSpinBox)
        self.panelLayout.addWidget(self.groupBoxParameter)
        self.panelLayout.addWidget(self.updateButton)
        self.panelLayout.addWidget(self.systemButton)
        self.panelLayout.addStretch()
