from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox
from PyQt6.QtMultimedia import QSoundEffect
from style import btn_style, selectlist_style
from constants import resolution_items
import sys
import winsound


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

        font_id = QFontDatabase.addApplicationFont("font_bold.ttf")
        families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(families[0], 24) if families else QFont("Arial", 24)
        font_big = QFont(families[0], 36) if families else QFont("Arial", 36) 
        # if families jest po to zeby jakby sie cos zwalilo ze tego fonta nie bedzie na kompie to zmieni sie na arial

        tytul.setFont(font_big)

        # Definiowanie zmieniania tego menu wiem ze cursed ale nie mialem lepszego pomyslu w sensie mialem ale nie chcialo mi sie uczyc 40 roznych innych rzeczy bo by mi to zajelo 2 lata a chcialem byc fair i nie kopiowac z chmurskiego nic wiec wyszedl monolit ktory zmienia visibility tego czegos
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
            resolution_label.show()
            graphics_settings.hide()
            audio_settings.hide()
            powrut.hide()
            powrut_settings.show()

        def powrot_graphics_settings():
            resolution.hide()
            resolution_label.hide()
            graphics_settings.show()
            audio_settings.show()
            powrut_settings.hide()
            powrut.show()

        # Splitnalem to co jest w arrayu z rozdzielczosciami zeby miec width i height oddzielnie zeby zrobic resize co ja bym zrobil bez lekcji o obsludze stringow na pso
        def change_resolution(text):
            res = text.split(' ')[0]
            width, height = res.split('x')
            self.resize(int(width), int(height))
        # klik (bardzo potrzebny comment)
        def click():
            winsound.PlaySound("clicked.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        single = QPushButton("Singleplayer")
        single.setStyleSheet(btn_style)
        single.setFixedWidth(500)
        single.setFont(font)
        single.clicked.connect(click)

        multi = QPushButton("Multiplayer")
        multi.setStyleSheet(btn_style)
        multi.setFixedWidth(500)
        multi.setFont(font)
        multi.clicked.connect(click)

        settings = QPushButton("Ustawienia")
        settings.setStyleSheet(btn_style)
        settings.setFixedWidth(500)
        settings.setFont(font)
        settings.clicked.connect(settings_window)
        settings.clicked.connect(click)

        btn_exit = QPushButton("Wyjdź z Diablo II")
        btn_exit.setStyleSheet(btn_style)
        btn_exit.setFixedWidth(500)
        btn_exit.setFont(font)
        btn_exit.clicked.connect(sys.exit)
        settings.clicked.connect(click)

        graphics_settings = QPushButton("Ustawienia Graficzne")
        graphics_settings.setStyleSheet(btn_style)
        graphics_settings.setFixedWidth(500)
        graphics_settings.setFont(font)
        graphics_settings.hide()
        graphics_settings.clicked.connect(graphics_settings_window)
        graphics_settings.clicked.connect(click)

        resolution_label = QLabel("Wybierz rozdzielczość:")
        resolution_label.setFixedWidth(500)
        resolution_label.setFont(font)
        resolution_label.hide()

        resolution = QComboBox()
        resolution.addItems(resolution_items)
        resolution.setStyleSheet(selectlist_style)
        resolution.setFixedWidth(500)
        resolution.setFont(font)
        resolution.setCurrentIndex(5)
        resolution.currentTextChanged.connect(change_resolution)
        resolution.hide()

        audio_settings = QPushButton("Ustawienia Audio")
        audio_settings.setStyleSheet(btn_style)
        audio_settings.setFixedWidth(500)
        audio_settings.setFont(font)
        audio_settings.clicked.connect(click)
        audio_settings.hide()

        powrut = QPushButton("Powrót")
        powrut.setStyleSheet(btn_style)
        powrut.setFixedWidth(500)
        powrut.setFont(font)
        powrut.clicked.connect(powrot_main)
        powrut.clicked.connect(click)
        powrut.hide()

        powrut_settings = QPushButton("Powrót")
        powrut_settings.setStyleSheet(btn_style)
        powrut_settings.setFixedWidth(500)
        powrut_settings.setFont(font)
        powrut_settings.clicked.connect(powrot_graphics_settings)
        powrut_settings.clicked.connect(click)
        powrut_settings.hide()

        layout.addStretch()
        layout.addWidget(tytul)
        layout.addSpacing(50)
        layout.addWidget(single, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(multi, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(settings, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(graphics_settings, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(resolution_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(resolution, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(audio_settings, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(powrut, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(powrut_settings, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.showFullScreen()