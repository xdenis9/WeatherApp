
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random

class Game (QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_label = QLabel("Enter a number between 1 - 100",self)
        self.guess_textbox = QLineEdit(self)
        self.guess_button = QPushButton("Guess!", self)
        self.result_label = QLabel(self)
        self.reset_button = QPushButton("reset",self)

        self.unitUI()

    
    def unitUI(self):
        self.setWindowTitle("Number Guessing Game")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Menu")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        file_menu.addAction(about_action)

        difficulty_action = QAction("Difficulty selector",self)
        difficulty_action.triggered.connect(self.difficulty)
        file_menu.addAction(difficulty_action)

        central_widget = QWidget(self) 
        self.setCentralWidget(central_widget)



        vbox = QVBoxLayout(central_widget)
        vbox.addWidget(self.main_label)

        vbox.addStretch(1)
        vbox.addWidget(self.guess_textbox)
        vbox.addStretch(1)
        
        vbox.addWidget(self.result_label)


        hbox = QHBoxLayout()
        hbox.addWidget(self.guess_button)
        hbox.addWidget(self.reset_button)
        

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.main_label.setAlignment(Qt.AlignCenter)
        self.guess_textbox.setAlignment(Qt.AlignCenter)
        #self.guess_button.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)



        self.guess_button.setFixedSize(150, 60)
        self.reset_button.setFixedSize(150, 60)

        self.main_label.setObjectName("main_label")
        self.guess_textbox.setObjectName("guess_textbox")
        self.guess_button.setObjectName("guess_button")
        self.result_label.setObjectName("result_label")
        self.reset_button.setObjectName("reset_button")

        self.setStyleSheet ("""
            QPushButton, QLineEdit, QLabel {
                font-family: Calibri;
            }
            QLabel#main_label {
                font-size: 50px;
                font-style: Italic;             
            }
            QLineEdit#guess_textbox {
                font-size: 40px;
                border: 2px solid hsl(43, 80%, 44%);
                border-radius: 5px;
                padding: 5px
            }
            QPushButton#guess_button {
                font-size: 30px;
                font-weight: bold;             
                background-color: orange;
                color: white;
                border-radius: 10px;
                padding: 5px;                        
            }
            QLabel#result_label {
                font-size: 50px;                                
            }
            QPushButton#reset_button {
                font-size: 20px;
                font-weight: bold;             
                background-color: #007BFF;
                color: white;
                border-radius: 10px;
                padding: 5px;
            }
            Game {
                background-color: hsl(217, 45%, 90%);
            }
            QPushButton#reset_button:hover {
                background-color: #0056b3;
            }
            QPushButton#guess_button:hover {
                background-color: #ff8c00;                 
            }
        """)
        self.guess_button.clicked.connect(self.nbr_generator)
        self.guess_textbox.returnPressed.connect(self.nbr_generator)
        self.reset_button.clicked.connect(self.reset)
        self.random_nbr()
    
    def show_about(self):
        QMessageBox.information(self, "About", "Number Guessing Game v1.0\nMade with PyQt5!")

    def difficulty (self):
        QMessageBox.addButton(self, "100-150",QPushButton)

    def random_nbr (self):
        self.random_nbr = random.randint(1,100)
        print(self.random_nbr)

    

    def nbr_generator(self):
        
        user_input = self.guess_textbox.text()

        if not user_input.isdigit():
            self.result_label.setText("Enter a valid number")
            self.guess_textbox.clear()
            return
        
        try:
            user_nbr = int(user_input)
            
        except ValueError:
            self.result_label.setText("Enter a valid number")
            self.guess_textbox.clear()


        if user_nbr < 0:
            self.result_label.setText("Negative numbers not allowed!")
            self.guess_textbox.clear()
        elif user_nbr > 100:
            self.result_label.setText("Under 100 please")
            self.guess_textbox.clear()
        elif user_nbr == 0:
            self.result_label.setText("No 0 please")
            self.guess_textbox.clear()

        else:       
            if self.random_nbr == user_nbr:
                self.result_label.setText(f"Congrats! {self.random_nbr} was the answer!")
                self.guess_button.setEnabled(False)
            elif self.random_nbr > user_nbr:
                self.result_label.setText("too low!")
            elif self.random_nbr < user_nbr:
                self.result_label.setText("too high!")

        

        
        self.guess_textbox.clear()
    def reset (self):
        self.guess_textbox.clear()
        self.result_label.clear()
        self.guess_button.setEnabled(True)
        self.random_nbr = random.randint(1,100)
        print(self.random_nbr)
        

   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec_())
