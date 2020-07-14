import sys

import PySide2.QtWidgets as qtw

from ui import MainWindow

# Создание Qt приложения
app = qtw.QApplication(sys.argv)
# Создание и вызов диалогового окна
ex_main_window = MainWindow()
# Запуск основного Qt цикла
sys.exit(app.exec_())
