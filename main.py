import sys
import requests
from PyQt5.QtWidgets import QApplication, QLineEdit, QComboBox, QPushButton, QLabel, QMainWindow, QErrorMessage
from PyQt5.QtGui import QIcon, QFont

curency = ["CZK", "EUR", "USD", "AUD", "CAD", "CHF", "JPY", "NZD", "GBP", "SEK", "DKK", "NOK", "SGD", "HKD", "MXN", "PLN", "RUB", "TRY", "ZAR", "CNH"]

# --Aplikace--
app = QApplication(sys.argv) # - Vytváří se instance třídy QApplication, která reprezentuje běžící aplikaci. Argument sys.argv obsahuje seznam argumentů předaných aplikaci z příkazové řádky.

# --Okno--
window = QMainWindow() # - Vytváří se instance hlavního okna aplikace pomocí třídy QMainWindow.
window.setWindowTitle("Převod měn 2.0")
window.setGeometry(100, 100, 310, 170)
window.setStyleSheet("background-color: #14085f")

# --Icona okna--
icon = QIcon("img/icon.ico")
window.setWindowIcon(icon)

# --Font--
font = QFont()
font.setPointSize(12)
font.setBold(False)


# --Widgety--
u_input = QLineEdit(window)
u_input.setStyleSheet("background-color: White")
u_input.move(10, 20)
u_input.resize(100, 30)
u_input.setFont(font)

# --Labely--
result_label = QLabel(window)
result_label.setStyleSheet("color: White")
result_label.resize(100, 30)
result_label.move(10, 60)
result_label.setText("0")
result_label.setFont(font)

kurz_label = QLabel(window)
kurz_label.setStyleSheet("color: White")
kurz_label.move(210, 60)
kurz_label.setText("kurz")
kurz_label.setFont(font)

notif_label = QLabel(window)
notif_label.setStyleSheet("color: White")
notif_label.move(10, 100)
notif_label.setFont(font)

# --Roletky--
drop_down_from = QComboBox(window)
drop_down_from.setStyleSheet("background-color: White")
drop_down_from.move(120, 20)
drop_down_from.resize(80, 30)
drop_down_from.setFont(font)

drop_down_to = QComboBox(window)
drop_down_to.setStyleSheet("background-color: White")
drop_down_to.move(120, 60)
drop_down_to.resize(80, 30)
drop_down_to.setFont(font)

for one_curency in curency:
    drop_down_from.addItem(one_curency)
    drop_down_to.addItem(one_curency)

# --Funkce--
def count():
    try:
        currency_from = drop_down_from.currentText()
        currency_to = drop_down_to.currentText()
        amount = float(u_input.text())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "UVUS8YM1zStOAYdqfwQPVFtq4frfGT2x"
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.setText(str(data_result["result"]))
        kurz_label.setText(str(data_result["info"]["rate"]))
        kurz_label.adjustSize()
        notif_label.setText("")
    except:
        notif_label.setText("Zadejte částku")
        notif_label.adjustSize()
        result_label.setText("0")
        kurz_label.setText("kurz")

        print(response.status_code)
        print(response.text)

# --Tlačítko--
button = QPushButton(window)
button.setText("Převést")
button.setStyleSheet("background-color: White")
button.move(210, 20)
button.resize(80, 30)
button.setFont(font)
button.clicked.connect(count)

window.show()
sys.exit(app.exec())
