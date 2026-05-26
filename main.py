# Sluchanie mommy asmr o 1 w nocy gotujac to - Peak zycia

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys


class SettingsWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Ustawienia")

        centralny = QWidget()
        self.setCentralWidget(centralny)
        centralny.setObjectName("centralny")
        centralny.setStyleSheet("QWidget#centralny { background-image: url('tlo_menu.jpg'); }")

        layout = QVBoxLayout()
        centralny.setLayout(layout)

        font_id = QFontDatabase.addApplicationFont("font_bold.ttf")
        families = QFontDatabase.applicationFontFamilies(font_id)

        btn_style = (
            "QPushButton{"
            "background-color: rgba(36, 33, 35, 153);"
            "padding: 20px;"
            "font-size: 18px;"
            "letter-spacing: 2px;"
            "color: white;"
            "}"
            "QPushButton:hover{"
            "background-color: rgba(36, 33, 35, 204);"
            "}"
            "QPushButton:pressed{"
            "background-color: rgba(36, 33, 35, 242);"
            "color: rgb(220, 220, 220);"
            "}"
        )

        tytul = QLabel("Ustawienia")
        tytul.setStyleSheet("background: none; letter-spacing: 10px; color: white;")
        tytul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tytul.setFont(QFont(families[0], 36))
        
        btn_powrot = QPushButton("Powrót")
        btn_powrot.setStyleSheet(btn_style)
        btn_powrot.setFixedWidth(500)
        btn_powrot.setFont(QFont(families[0], 24))
        btn_powrot.clicked.connect(self.powrot)

        layout.addStretch()
        layout.addWidget(tytul)
        layout.addSpacing(50)
        layout.addWidget(btn_powrot, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.showFullScreen()

    def powrot(self):
        self.main_window.show()
        self.close()
    


def main_menu():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Diablo II")

            centralny = QWidget()
            self.setCentralWidget(centralny)

            layout = QVBoxLayout()
            centralny.setLayout(layout)
            centralny.setObjectName("centralny")
            centralny.setStyleSheet("QWidget#centralny { background-image: url('tlo_menu.jpg'); }")

            tytul = QLabel("Diablo II")
            tytul.setStyleSheet("background: none; letter-spacing: 10px; color: white;")
            tytul.setAlignment(Qt.AlignmentFlag.AlignCenter)

            btn_style = (
                "QPushButton{"
                "background-color: rgba(36, 33, 35, 153);"
                "padding: 20px;"
                "font-size: 18px;"
                "letter-spacing: 2px;"
                "color: white;"
                "}"
                "QPushButton:hover{"
                "background-color: rgba(36, 33, 35, 204);"
                "}"
                "QPushButton:pressed{"
                "background-color: rgba(36, 33, 35, 242);"
                "color: rgb(220, 220, 220);"
                "}"
            )

            font_id = QFontDatabase.addApplicationFont("font_bold.ttf")
            families = QFontDatabase.applicationFontFamilies(font_id)

            single = QPushButton("Singleplayer")
            single.setStyleSheet(btn_style)
            single.setFixedWidth(500)

            multi = QPushButton("Multiplayer")
            multi.setStyleSheet(btn_style)
            multi.setFixedWidth(500)

            settings = QPushButton("Ustawienia")
            settings.setStyleSheet(btn_style)
            settings.setFixedWidth(500)
            settings.clicked.connect(self.open_settings)

            btn_exit = QPushButton("Wyjdź z Diablo II")
            btn_exit.setStyleSheet(btn_style)
            btn_exit.setFixedWidth(500)
            btn_exit.clicked.connect(sys.exit)

            single.setFont(QFont(families[0], 24))
            multi.setFont(QFont(families[0], 24))
            tytul.setFont(QFont(families[0], 36))
            settings.setFont(QFont(families[0], 24))
            btn_exit.setFont(QFont(families[0], 24))

            # The layout of doom and despair
            layout.addStretch()
            layout.addWidget(tytul)
            layout.addSpacing(50)
            layout.addWidget(single, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(multi, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch() # To ogolnie mi chmurski powiedzial zeby dodac, to wywala taki nieprzyjemny space pod tymi przyciskami, cholera wie o co z tym chodzi ale trzeba to dodac bo inaczej wybuchnie

            self.showFullScreen()

        def open_settings(self):
            self.sw = SettingsWindow(self)
            self.sw.show()
            self.hide()

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) # Nie usuwac tej linijki bo sie zbombarduje


main_menu()