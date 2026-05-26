# Sluchanie mommy asmr o 1 w nocy gotujac to - Peak zycia

from PyQt6.QtGui import QPixmap, QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

def main_menu():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Diablo II")
            self.setStyleSheet("background-image: url('tlo_menu.jpg'); color: white;")

            # QMainWindow wymaga centralnego widgetu cosik jak taki container
            centralny = QWidget()
            self.setCentralWidget(centralny)

            layout = QVBoxLayout()
            centralny.setLayout(layout)

            # Logo
            tytul = QLabel()
            tytul_img = QPixmap('diablo_logo.png')
            tytul.setPixmap(tytul_img)
            tytul.setStyleSheet("background: none;")
            tytul.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Przyciski
            btn_style = "background-color: #333; padding: 20px; font-size: 18px;"
            font_id = QFontDatabase.addApplicationFont("Outfit-bold.ttf")
            families = QFontDatabase.applicationFontFamilies(font_id)

            single = QPushButton("Singleplayer")
            single.setStyleSheet(btn_style)
            single.setFixedWidth(500)

            multi = QPushButton("Multiplayer")
            multi.setStyleSheet(btn_style)
            multi.setFixedWidth(500)

            single.setFont(QFont(families[0], 24))
            multi.setFont(QFont(families[0], 24))

            # The layout of doom and despair
            layout.addStretch()
            layout.addWidget(tytul)
            layout.addSpacing(50)
            layout.addWidget(single, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(multi, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch() # To ogolnie mi chmurski powiedzial zeby dodac, to wywala taki nieprzyjemny space pod tymi przyciskami, cholera wie o co z tym chodzi ale trzeba to dodac bo inaczej wybuchnie

            self.showFullScreen()

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

main_menu()