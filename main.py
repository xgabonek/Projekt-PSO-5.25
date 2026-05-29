# Sluchanie mommy asmr o 1 w nocy gotujac to - Peak zycia

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox
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

            # Style stylunie stylusie
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

            selectlist_style = (
                "QComboBox {"
                "background-color: rgba(36, 33, 35, 153);"
                "padding: 20px;"
                "font-size: 18px;"
                "letter-spacing: 2px;"
                "color: white;"
                "border: none;"
                "}"

                "QComboBox:hover {"
                "background-color: rgba(36, 33, 35, 204);"
                "}"

                "QComboBox::drop-down {"
                "border: none;"
                "width: 40px;"
                "}"
                "QComboBox::down-arrow {"
                "image: url('arrow.png');"
                "width: 16px;"
                "height: 16px;"
                "}"

                "QComboBox QAbstractItemView {"
                "background-color: rgba(36, 33, 35, 230);"
                "color: white;"
                "selection-background-color: rgba(180, 50, 50, 200);"
                "selection-color: white;"
                "border: 1px solid rgba(255,255,255,30);"
                "padding: 5px;"
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
            
            # Funkcje funkcyjki na menu
            def settings_window():
                single.hide()
                multi.hide()
                settings.hide()
                btn_exit.hide()
                graphics_settings.show()
                audio_settings.show()
                powrut.show()

            def powrot_main():
                single.show()
                multi.show()
                settings.show()
                btn_exit.show()
                graphics_settings.hide()
                audio_settings.hide()
                powrut.hide()

            def graphics_settings_window():
                resolution.show()
                graphics_settings.hide()
                audio_settings.hide()
                powrut.hide()
                powrut_settings.show()

            def powrot_graphics_settings():
                resolution.hide()
                graphics_settings.show()
                audio_settings.show()
                powrut_settings.hide()
                powrut.show()

            def change_resolution(text):
                res = text.split(' ')[0] # zamysl jest taki zeby wyciagac width i height osobno splitem
                width, height = res.split('x') # dodalem x do splita zeby rozdzielic width i height xem bo byloby 19201080 a to by bylo szponckie i niemile
                self.resize(int(width), int(height))



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
            graphics_settings.clicked.connect(graphics_settings_window)

            # Array na rozdzielczosci od chmurskiego
            resolution_items = [
                # 21:9 Ultrawide
                '5120x2160 (21:9)',
                '3440x1440 (21:9)',
                '2560x1080 (21:9)',
                # 16:9
                '3840x2160 (16:9)',  # 4K
                '2560x1440 (16:9)',
                '1920x1080 (16:9)',
                '1600x900 (16:9)',
                '1366x768 (16:9)',
                '1280x720 (16:9)',
                # 16:10
                '2560x1600 (16:10)',
                '1920x1200 (16:10)',
                '1680x1050 (16:10)',
                '1440x900 (16:10)',
                '1280x800 (16:10)',
                # 4:3
                '1600x1200 (4:3)',
                '1400x1050 (4:3)',
                '1280x960 (4:3)',
                '1024x768 (4:3)',
                '800x600 (4:3)',
            ]

            resolution = QComboBox()
            resolution.addItems(resolution_items)
            resolution.setStyleSheet(selectlist_style)
            resolution.setFixedWidth(500)
            resolution.currentTextChanged.connect(change_resolution)
            resolution.hide()
            


            audio_settings = QPushButton("Ustawienia Audio")
            audio_settings.setStyleSheet(btn_style)
            audio_settings.setFixedWidth(500)
            audio_settings.hide()

            powrut = QPushButton("Powrót")
            powrut.setStyleSheet(btn_style)
            powrut.setFixedWidth(500)
            powrut.clicked.connect(powrot_main)
            powrut.hide()

            powrut_settings = QPushButton("Powrót")
            powrut_settings.setStyleSheet(btn_style)
            powrut_settings.setFixedWidth(500)
            powrut_settings.clicked.connect(powrot_graphics_settings)
            powrut_settings.hide()

            # Ustawianie Fonta dla wszystkiego ignore it tbh
            single.setFont(QFont(families[0], 24))
            multi.setFont(QFont(families[0], 24))
            tytul.setFont(QFont(families[0], 36))
            settings.setFont(QFont(families[0], 24))
            btn_exit.setFont(QFont(families[0], 24))
            graphics_settings.setFont(QFont(families[0], 24))
            audio_settings.setFont(QFont(families[0], 24))
            powrut.setFont(QFont(families[0], 24))
            resolution.setFont(QFont(families[0], 24))
            powrut_settings.setFont(QFont(families[0], 24))

            # The layout of doom and despair
            layout.addStretch()
            layout.addWidget(tytul)
            layout.addSpacing(50)
            layout.addWidget(single, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(multi, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(graphics_settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(resolution, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(audio_settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(powrut, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(powrut_settings, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch() # To ogolnie mi chmurski powiedzial zeby dodac, to wywala taki nieprzyjemny space pod tymi przyciskami, cholera wie o co z tym chodzi ale trzeba to dodac bo inaczej wybuchnie

            self.showFullScreen()

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


main_menu()