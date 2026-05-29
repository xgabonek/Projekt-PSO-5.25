from PyQt6.QtWidgets import QApplication
from windows import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())