import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class SPO_Widget(QWidget):
    def __init__(self):
        super().__init__()
        # GUI creator
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.resize(800, 500)
        self.center()
        self.setWindowTitle('SPO')
        self.setWindowIcon(QIcon("web.png"))

    # center widget on desktop
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # # confirm close widget
    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Message',
    #                                  "Are you sure to quit?", QMessageBox.Yes |
    #                                  QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SPO_Widget()
    # ex.show()
    sys.exit(app.exec_())
