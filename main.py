from PyQt6.QtWidgets import QApplication
from gui import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())