from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from calculator import Calculator


class CalculatorWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.calculator = Calculator()

        self.setWindowTitle("MVC Calculator")

        self.layout = QGridLayout()

        self.input = QLineEdit()
        self.layout.addWidget(self.input, 0, 0, 1, 4)

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
        ]

        for text,row,col in buttons:
            button = QPushButton(text)
            self.layout.addWidget(button,row,col)

            if text == "=":
                button.clicked.connect(self.calculate)
            elif text == "C":
                button.clicked.connect(self.clear)
            else:
                button.clicked.connect(lambda _, t=text: self.add_char(t))

        self.setLayout(self.layout)

    def add_char(self, char):
        self.calculator.add_to_expression(char)
        self.input.setText(self.calculator.get_expression())

    def calculate(self):
        result = self.calculator.calculate()
        self.input.setText(str(result))

    def clear(self):
        self.calculator.clear_expression()
        self.input.setText("")