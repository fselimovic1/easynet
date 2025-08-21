from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Easy Net")

        # Create the tab widget
        tabs = QTabWidget()

        # First tab (just a QWidget with a layout)
        tab1 = QWidget()
        # Second tab
        tab2 = QWidget()


        # Add tabs to the QTabWidget
        tabs.addTab(tab1, "Status")
        tabs.addTab(tab2, "Configuration")

        # Set central widget of main window
        self.setCentralWidget(tabs)
