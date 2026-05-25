# Robienie pieknej aklipacji w PyQt6 oczywiscie na sluchawkach DJ peirdolony rak watroby
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMainWindow, QLabel
import sys

def main_menu():
    # QApplication potrzebuje sys zeby zadowolic niektore argumenty CLI, albo np. sys.exit() zeby zapewnic sobie czysty shutdown itp
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__() # super() bylo po to zeby dziedziczona klasa mogla korzystac z funkcji rodzica

            # Tutaj ustawienia okienka elegancko pykpykpyk wszystko wsm to straight forward
            self.setWindowTitle("Diablo II")
            tytul = QLabel(self)
            tytul_img = QPixmap('diablo_logo.png')
            tytul.setPixmap(tytul_img)
            tytul.resize(750, 150)
            tytul.move(585, 75)
            tytul.setAlignment(Qt.AlignmentFlag.AlignCenter)
            single = QPushButton(self)
            single = QLabel(self)
            single_img = QPixmap('singplayer_button.png')
            single.setPixmap(single_img)
            single.resize(500, 75)
            single.move(710, 350)
            multi = QLabel(self)
            multi.resize(500, 75)
            multi.move(710, 425)

            self.showFullScreen()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

main_menu()

# Godzina 11:03 dnia 05/25/2026 historycznie pierwsze działające okienko.