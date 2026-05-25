from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

def main_menu():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Diablo II")
            self.setStyleSheet("background-color: #222; color: white;")

            # QMainWindow wymaga centralnego widgetu cosik jak taki container
            centralny = QWidget()
            self.setCentralWidget(centralny)

            layout = QVBoxLayout()
            centralny.setLayout(layout)

            # Logo
            tytul = QLabel()
            tytul_img = QPixmap('diablo_logo.png')
            tytul.setPixmap(tytul_img)
            tytul.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Przyciski
            btn_style = "background-color: #333; padding: 20px; font-size: 18px;"

            single = QPushButton("Singleplayer")
            single.setStyleSheet(btn_style)
            single.setFixedWidth(500)

            multi = QPushButton("Multiplayer")
            multi.setStyleSheet(btn_style)
            multi.setFixedWidth(500)

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