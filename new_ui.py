import sys
from PyQt5.QtWidgets import *
import design


class Example(design.UIForm):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        # self.show_result()

    # def show_result(self):
    #     self.pushbutton.clicked.connect(self.on_button_click)
    #
    # def on_button_click(self, event):
    #     pass


def main():
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
