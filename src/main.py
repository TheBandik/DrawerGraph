import sys

from PySide2.QtWidgets import QApplication

from ui.mainwindow import MainWindow

# Создание Qt приложения
app = QApplication(sys.argv)
# Создание и вызов окна
ex_main_window = MainWindow()
# Запуск основного Qt цикла
sys.exit(app.exec_())
