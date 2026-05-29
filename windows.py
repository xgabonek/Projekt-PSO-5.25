from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox
from style import btn_style, selectlist_style
from constants import resolution_items


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

        tytul.setFont(font_big)

        single = QPushButton("Singleplayer")
        single.setStyleSheet(btn_style)
        single.setFixedWidth(500)
        single.setFont(font)

        multi = QPushButton("Multiplayer")
        multi.setStyleSheet(btn_style)
        multi.setFixedWidth(500)
        multi.setFont(font)

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

        def change_resolution(text):
            res = text.split(' ')[0]
            width, height = res.split('x')
            self.resize(int(width), int(height))

        settings = QPushButton("Ustawienia")
        settings.setStyleSheet(btn_style)
        settings.setFixedWidth(500)
        settings.setFont(font)
        settings.clicked.connect(settings_window)

        btn_exit = QPushButton("Wyjdź z Diablo II")
        btn_exit.setStyleSheet(btn_style)
        btn_exit.setFixedWidth(500)
        btn_exit.setFont(font)
        btn_exit.clicked.connect(lambda: __import__('sys').exit())

        graphics_settings = QPushButton("Ustawienia Graficzne")
        graphics_settings.setStyleSheet(btn_style)
        graphics_settings.setFixedWidth(500)
        graphics_settings.setFont(font)
        graphics_settings.hide()
        graphics_settings.clicked.connect(graphics_settings_window)

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
        audio_settings.hide()

        powrut = QPushButton("Powrót")
        powrut.setStyleSheet(btn_style)
        powrut.setFixedWidth(500)
        powrut.setFont(font)
        powrut.clicked.connect(powrot_main)
        powrut.hide()

        powrut_settings = QPushButton("Powrót")
        powrut_settings.setStyleSheet(btn_style)
        powrut_settings.setFixedWidth(500)
        powrut_settings.setFont(font)
        powrut_settings.clicked.connect(powrot_graphics_settings)
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