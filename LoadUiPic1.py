"""
@FileName：LoadUiPic1.py
@Description：
@Author：Eric
@Time：11/23/2021 4:03 AM

"""

import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtCore import QFile, QIODevice

class LoadUiPic1(object):


    def __init__(self, MainWindow):
        self.ui = QUiLoader().load('./ui/pic1.ui')
        self.ui.btn_search.clicked.connect(self.print_search)
        self.ui.actionABOUT.triggered.connect(self.print_about)
        self.ui.actionTODO.triggered.connect(self.print_todo)
        self.ui.actionTODO2.triggered.connect(self.print_todo2)


    # search button action
    def print_search(self):
        text = self.ui.ipt_person.text()
        QMessageBox.about(self.ui, "Prompt", "You just searched :" + text)
        print(text)

# about action
    def print_about(self):
        QMessageBox.about(self.ui, "Prompt", "Author :" + "Eric.H")

# Todo action
    def print_todo(self):
        QMessageBox.about(self.ui, "Prompt", "TODO")

# todo2 action
    def print_todo2(self):
        QMessageBox.about(self.ui, "Prompt", "TODO2")
