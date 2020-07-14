import PySide2.QtWidgets as qtw
import PySide2.QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.main_window_ui()
        self.show()

    def main_window_ui(self):
        self.setWindowTitle("Graph")
        self.resize(640, 480)
        # TODO иконка
        # icon_main_window = QIcon("icon_main_window.png")
        # self.setWindowIcon(icon_main_window)

        # Макеты
        self.main_layout = qtw.QHBoxLayout()
        self.widget_layout = qtw.QVBoxLayout()
        self.group_box_parameter_layout = qtw.QVBoxLayout()
        self.setLayout(self.main_layout)
        # Фрейм
        self.frame = qtw.QFrame()
        self.frame.setMinimumSize(qtc.QSize(200, 200))
        # Виджет
        self.widget = qtw.QWidget()
        self.widget.setMinimumSize(qtc.QSize(200, 0))
        self.widget.setMaximumSize(qtc.QSize(200, 1000000))
        self.widget.setLayout(self.widget_layout)
        # Параметр
        self.group_box_parameter = qtw.QGroupBox("Parameter", self.widget)
        self.group_box_parameter.setLayout(self.group_box_parameter_layout)
        self.double_spin_box = qtw.QDoubleSpinBox(self.group_box_parameter)
        # Кнопки
        self.update_button = qtw.QPushButton("Update", self.widget)
        self.system_button = qtw.QPushButton("System", self.widget)
        # Добавление виджетов в макет
        self.main_layout.addWidget(self.frame)
        self.main_layout.addWidget(self.widget)
        self.group_box_parameter_layout.addWidget(self.double_spin_box)
        self.widget_layout.addWidget(self.group_box_parameter)
        self.widget_layout.addWidget(self.update_button)
        self.widget_layout.addWidget(self.system_button)
        self.widget_layout.addStretch()
