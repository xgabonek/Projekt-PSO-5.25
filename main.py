# Robienie pieknej aklipacji w PyQt6 oczywiscie na sluchawkach DJ peirdolony rak watroby
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMainWindow
import sys

def main_menu():
    # QApplication potrzebuje sys zeby zadowolic niektore argumenty CLI, albo np. sys.exit() zeby zapewnic sobie czysty shutdown itp
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__() # super() bylo po to zeby dziedziczona klasa mogla korzystac z funkcji rodzica

            # Tutaj ustawienia okienka elegancko pykpykpyk wszystko wsm to straight forward
            self.setWindowTitle("Okienko")
            dupa1 = QPushButton("dupa1", self)
            self.setFixedSize(QSize(700, 400))
            dupa1.resize(200, 50)
            dupa1.move(250, 100)
            dupa2 = QPushButton("dupa2", self)
            dupa2.resize(200, 50)
            dupa2.move(250, 175)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

main_menu()

# Godzina 11:03 dnia 05/25/2026 historycznie pierwsze działające okienko.