"""
@FileName：pic1main.py
@Description：
@Author：Eric
@Time：11/23/2021 2:07 AM

"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_pic1 import Ui_MainWindow

Author = "Eric.H"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# search button action
    def print_search(self):
        text = self.ui.ipt_person.text()
        QMessageBox.about(self, "Prompt", "You just searched :" + text)
        print(text)

# about action
    def print_about(self):
        QMessageBox.about(self, "Prompt", "Author :" + Author)

# Todo action
    def print_todo(self):
        QMessageBox.about(self, "Prompt", "TODO")

# todo2 action
    def print_todo2(self):
        QMessageBox.about(self, "Prompt", "TODO2")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())