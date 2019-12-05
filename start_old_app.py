from PyQt5 import QtWidgets
import sys

import labels


class App(QtWidgets.QMainWindow, labels.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
