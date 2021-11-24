"""
@FileName：loaderMain.py
@Description：
@Author：Eric
@Time：11/23/2021 4:07 AM

"""
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtCore import QFile, QIODevice
from LoadUiPic1 import LoadUiPic1





if __name__ == "__main__":
    '''
    @Description：function main()
    '''
    app = QApplication([])
    UI = LoadUiPic1(app)
    UI.ui.show()
    app.exec()

