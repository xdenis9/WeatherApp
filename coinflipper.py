
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
import time

class Flipper(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = QLabel("Heads or tails?",self)
        self.answer_input = QLineEdit(self)
        self.answer_button = QPushButton ("Flip a coin!",self)
        self.result_label = QLabel("Result",self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Coin Flipper")

        vbox = QVBoxLayout()
        vbox.addWidget(self.main_label)
        vbox.addWidget(self.answer_input)
        vbox.addWidget(self.answer_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

        self.main_label.setAlignment(Qt.AlignCenter)
        self.answer_input.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.main_label.setObjectName("main_label")
        self.answer_input.setObjectName("answer_input")
        self.answer_button.setObjectName("answer_button")
        self.result_label.setObjectName("result_label")

        self.setStyleSheet("""
            QLabel, QPushButton, QLineEdit {
                font-family: Calibri;
                font-size: 50px;                
            }

        """)
        self.answer_button.clicked.connect(self.update_result)
        self.answer_input.returnPressed.connect(self.update_result)


    def update_result (self):
        user_input = self.answer_input.text().lower()

        self.result_label.setMovie(QMovie("weather app\giphy.webp"))
        self.result_label.movie().start()

        QTimer.singleShot(2000, lambda: self.show_result(user_input))



    def show_result(self, user_input):
        list_of_results = ("heads", "tails")
        result = random.choice(list_of_results)
        print(result)
        if  user_input == result:
            self.result_label.setText("Win!")
        else:
            self.result_label.setText("Lose!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    flipper = Flipper()
    flipper.show()
    sys.exit(app.exec_())