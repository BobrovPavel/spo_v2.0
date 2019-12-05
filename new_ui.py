import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import design


class Example(lab.UIForm):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        # self.resize(693, 478)
        # self.setStyleSheet("")
        # self.show_result()
        self.show_result()

    def show_result(self):
        self.pushbutton.clicked.connect(self.on_click)

    def on_click(self):
        self.tabWidget.hide()

def main():
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
