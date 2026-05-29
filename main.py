# Sluchanie mommy asmr o 1 w nocy gotujac to - Peak zycia

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
    

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
            

            def settings_window():
                single.hide()
                multi.hide()
                settings.hide()
                graphics_settings.show()
                audio_settings.show()
                powrut.show()
                btn_exit.hide()

            def powrot_main():
                single.show()
                multi.show()
                settings.show()
                graphics_settings.hide()
                audio_settings.hide()
                powrut.hide()
                btn_exit.show()

            settings = QPushButton("Ustawienia")
            settings.setStyleSheet(btn_style)
            settings.setFixedWidth(500)
            settings.clicked.connect(settings_window)


            btn_exit = QPushButton("Wyjdź z Diablo II")
            btn_exit.setStyleSheet(btn_style)
            btn_exit.setFixedWidth(500)
            btn_exit.clicked.connect(sys.exit)

            # Ustawienia
            graphics_settings = QPushButton("Ustawienia Graficzne")
            graphics_settings.setStyleSheet(btn_style)
            graphics_settings.setFixedWidth(500)
            graphics_settings.hide()

            audio_settings = QPushButton("Ustawienia Audio")
            audio_settings.setStyleSheet(btn_style)
            audio_settings.setFixedWidth(500)
            audio_settings.hide()

            powrut = QPushButton("Powrót")
            powrut.setStyleSheet(btn_style)
            powrut.setFixedWidth(500)
            powrut.clicked.connect(powrot_main)
            powrut.hide()

            single.setFont(QFont(families[0], 24))
            multi.setFont(QFont(families[0], 24))
            tytul.setFont(QFont(families[0], 36))
            settings.setFont(QFont(families[0], 24))
            btn_exit.setFont(QFont(families[0], 24))
            graphics_settings.setFont(QFont(families[0], 24))
            audio_settings.setFont(QFont(families[0], 24))
            powrut.setFont(QFont(families[0], 24))

            # The layout of doom and despair
            layout.addStretch()
            layout.addWidget(tytul)
            layout.addSpacing(50)
            layout.addWidget(single, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(multi, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(graphics_settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(audio_settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(powrut, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch() # To ogolnie mi chmurski powiedzial zeby dodac, to wywala taki nieprzyjemny space pod tymi przyciskami, cholera wie o co z tym chodzi ale trzeba to dodac bo inaczej wybuchnie

            self.showFullScreen()

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


main_menu()