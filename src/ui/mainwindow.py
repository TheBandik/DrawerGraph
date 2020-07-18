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
        self.resize(700, 380)
        # Макеты
        self.mainLayout = QHBoxLayout()
        self.panelLayout = QVBoxLayout()
        self.groupBoxParameterLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        # Панель
        self.panel = QWidget()
        self.panel.setMinimumSize(QSize(200, 0))
        self.panel.setMaximumSize(QSize(200, 1000000))
        self.panel.setLayout(self.panelLayout)
        # Параметр
        self.groupBoxParameter = QGroupBox("Parameter", self.panel)
        self.groupBoxParameter.setLayout(self.groupBoxParameterLayout)
        self.doubleSpinBox = QDoubleSpinBox(self.groupBoxParameter)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(100.0)
        self.doubleSpinBox.setValue(3.0)
        self.a = self.doubleSpinBox.value()
        # Кнопки
        self.updateButton = QPushButton("Update", self.panel)
        self.systemButton = QPushButton("System", self.panel)
        # Действие кнопки
        self.updateButton.clicked.connect(self.updateIsClicked)
        # Виджет
        self.graphWidget = GraphWidget(self.a)
        # Добавление виджетов в макет
        self.mainLayout.addWidget(self.graphWidget)
        self.mainLayout.addWidget(self.panel)
        self.groupBoxParameterLayout.addWidget(self.doubleSpinBox)
        self.panelLayout.addWidget(self.groupBoxParameter)
        self.panelLayout.addWidget(self.updateButton)
        self.panelLayout.addWidget(self.systemButton)
        self.panelLayout.addStretch()

    def updateIsClicked(self):
        self.a = self.doubleSpinBox.value()
        self.graphWidget.setParams(self.a)
