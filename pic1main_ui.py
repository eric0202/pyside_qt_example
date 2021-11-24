"""
@FileName：pic1main_ui.py
@Description：
@Author：Eric
@Time：11/23/2021 3:28 AM

"""

# File: main.py
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "./ui/pic1.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()


    # search button action
    def print_search(self):
        text = self.ipt_person.text()
        QMessageBox.about(self, "Prompt", "You just searched :" + text)
        print(text)




    sys.exit(app.exec())

