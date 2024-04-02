import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ('7', 1, 0),
            ('8', 1, 1),
            ('9', 1, 2),
            ('/', 1, 3),
            ('4', 2, 0),
            ('5', 2, 1),
            ('6', 2, 2),
            ('*', 2, 3),
            ('1', 3, 0),
            ('2', 3, 1),
            ('3', 3, 2),
            ('-', 3, 3),
            ('C', 4, 0),
            ('0', 4, 1),
            ('=', 4, 2),
            ('+', 4, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            button.setStyleSheet(
                "background-color: #FFA500; color: black; font-size: 18px; padding: 20px; border: 1px solid black;")
            self.layout.addWidget(button, row, col)

        self.setStyleSheet("background-color: black; color: white;")

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            self.calculate()
        elif text == 'C':
            self.clear_clicked()
        else:
            self.display.setText(self.display.text() + text)

    def clear_clicked(self):
        self.display.clear()

    def calculate(self):
        expression = self.display.text()
        try:
            result = eval(expression)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
