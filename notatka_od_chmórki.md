# PyQt6 — Notatka

## Szkielet aplikacji

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tytuł okienka")
        self.setFixedSize(800, 600)  # szerokość, wysokość w pikselach

app = QApplication(sys.argv)  # sys.argv żeby Qt wiedziało o argumentach CLI
window = MainWindow()
window.show()
sys.exit(app.exec())  # sys.exit() żeby mieć czysty shutdown
```

---

## Rozmiar i pozycja okna

```python
self.setFixedSize(800, 600)        # stały rozmiar, nie można rozciągać
self.resize(800, 600)              # domyślny rozmiar, można rozciągać
self.move(100, 100)                # pozycja okna na ekranie (x, y)
self.setMinimumSize(400, 300)      # minimalny rozmiar
self.setMaximumSize(1200, 900)     # maksymalny rozmiar
```

---

## Widgety — podstawowe elementy

### QPushButton — przycisk

```python
from PyQt6.QtWidgets import QPushButton

btn = QPushButton("Kliknij mnie", self)
btn.resize(150, 40)          # rozmiar przycisku
btn.move(50, 50)             # pozycja (x, y) względem okna

# Podpięcie akcji pod kliknięcie
btn.clicked.connect(self.moja_funkcja)

def moja_funkcja(self):
    print("Kliknięto!")
```

### QLabel — tekst / etykieta

```python
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

label = QLabel("Hej!", self)
label.move(50, 100)
label.resize(200, 30)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # wyśrodkowanie tekstu
label.setText("Nowy tekst")  # zmiana tekstu po stworzeniu
```

### QLineEdit — pole tekstowe (jedna linia)

```python
from PyQt6.QtWidgets import QLineEdit

pole = QLineEdit(self)
pole.move(50, 150)
pole.resize(200, 30)
pole.setPlaceholderText("Wpisz coś...")  # szary tekst podpowiedzi
tekst = pole.text()                       # pobranie wpisanego tekstu
pole.setText("domyślna wartość")          # ustawienie tekstu
```

### QTextEdit — pole tekstowe (wiele linii)

```python
from PyQt6.QtWidgets import QTextEdit

obszar = QTextEdit(self)
obszar.move(50, 200)
obszar.resize(300, 150)
obszar.setPlainText("Jakiś tekst")
tekst = obszar.toPlainText()  # pobranie tekstu
```

---

## Pozycjonowanie

### Ręczne (absolutne) — `.move(x, y)`

Najprostsze, ale sztywne. Pozycja liczona od lewego górnego rogu okna.

```python
btn.move(50, 50)    # 50px od lewej, 50px od góry
```

### Layout — automatyczne układanie

Lepsze podejście — elementy same się układają i skalują z oknem.

```python
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

# Potrzebny centralny widget w QMainWindow
container = QWidget()
self.setCentralWidget(container)

# QVBoxLayout — układa w kolumnie (jeden pod drugim)
layout = QVBoxLayout()
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(label)

# QHBoxLayout — układa w rzędzie (obok siebie)
layout_poziomy = QHBoxLayout()
layout_poziomy.addWidget(btn_lewy)
layout_poziomy.addWidget(btn_prawy)

# Zagnieżdżanie layoutów
glowny = QVBoxLayout()
glowny.addLayout(layout_poziomy)  # rząd przycisków
glowny.addWidget(label)           # etykieta pod spodem

container.setLayout(glowny)
```

---

## Czcionka i styl

```python
from PyQt6.QtGui import QFont

# Ustawienie czcionki na widgecie
font = QFont("Arial", 14)
font.setBold(True)
label.setFont(font)

# Stylowanie przez CSS (setStyleSheet)
btn.setStyleSheet("background-color: blue; color: white; border-radius: 5px;")
label.setStyleSheet("font-size: 18px; color: red;")
```

---

## Komunikacja między widgetami (sygnały)

```python
# Przycisk → funkcja
btn.clicked.connect(self.on_click)

# Pole tekstowe → funkcja przy każdej zmianie
pole.textChanged.connect(self.on_text_change)

# Pole tekstowe → funkcja po wciśnięciu Enter
pole.returnPressed.connect(self.on_enter)

def on_click(self):
    tekst = self.pole.text()
    self.label.setText(f"Wpisałeś: {tekst}")
```

---

## Okna dialogowe

```python
from PyQt6.QtWidgets import QMessageBox

# Proste okno z komunikatem
QMessageBox.information(self, "Tytuł", "Treść wiadomości")
QMessageBox.warning(self, "Uwaga", "Coś poszło nie tak!")
QMessageBox.critical(self, "Błąd", "Krytyczny błąd!")

# Okno z pytaniem (tak/nie)
odpowiedz = QMessageBox.question(self, "Pytanie", "Czy chcesz wyjść?")
if odpowiedz == QMessageBox.StandardButton.Yes:
    self.close()
```

---

## Przykład z wszystkim razem

```python
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                              QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja apka")
        self.setFixedSize(400, 300)

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout()

        self.label = QLabel("Wpisz coś poniżej:")
        self.pole = QLineEdit()
        self.pole.setPlaceholderText("Tu wpisz tekst...")
        self.btn = QPushButton("Potwierdź")
        self.btn.clicked.connect(self.on_click)

        layout.addWidget(self.label)
        layout.addWidget(self.pole)
        layout.addWidget(self.btn)
        container.setLayout(layout)

    def on_click(self):
        tekst = self.pole.text()
        self.label.setText(f"Wpisałeś: {tekst}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
```