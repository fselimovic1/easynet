from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
import sys

def run():
    app = QApplication(sys.argv)
    win = MainWindow(app)
    win.show()
    sys.exit(app.exec())
