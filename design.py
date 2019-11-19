from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog

from hdd_info import DiskInfo


class UIForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(693, 478)
        self.setStyleSheet("")
        self.disk = DiskInfo()

    def setup_ui(self):
        self.mainwidget = QtWidgets.QWidget(self)
        self.mainwidget.setGeometry(QtCore.QRect(40, 80, 592, 131))
        self.mainwidget.setObjectName("mainwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.mainwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.show_disk_table_headers()
        self.show_disk_form()

        self.pushbutton = QtWidgets.QPushButton("Analize", self.mainwidget)
        self.pushbutton.setObjectName("pushbutton")
        self.pushbutton.setStyleSheet("margin-top: 15px; font-size: 22px;")
        self.gridLayout.addWidget(self.pushbutton, 4, 5)

        # self.retranslateUi(Form)
        self.mainwidget.setLayout(self.gridLayout)
        QtCore.QMetaObject.connectSlotsByName(self)

    # def retranslateUi(self, Form):
    #     pass
    #     # self.label_2.setText("D")
    #     # self.label.setText("C")

    def show_disk_table_headers(self):
        headers = ["Total", "Used", "Free", "Percent"]
        self.draw_disk_table_headers(headers)

    def draw_disk_table_headers(self, headers):
        position = 2
        for header in headers:
            title = QtWidgets.QLabel(self.mainwidget)
            title.setStyleSheet("font-size:18px; margin: 2px auto;")
            title.setText(header)
            title.setObjectName("header")
            self.gridLayout.addWidget(title, 0, position)
            position += 1

    def draw_disk_info_row(self, position_x, position_y, value):
        text_edit = QtWidgets.QTextEdit(self.mainwidget)
        text_edit.setStyleSheet("font-size: 17px;")
        text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(text_edit, position_x, position_y)
        text_edit.setText(value)

    def show_disk_form(self):
        string_number = 1
        for disk in self.disk.get_all_devices():
            label = QtWidgets.QLabel(self.mainwidget)
            label.setStyleSheet("font-size: 20px; margin: auto 2px;")
            label.setObjectName("label")
            self.gridLayout.addWidget(label, string_number, 1)
            label.setText(disk)
            self.draw_disk_info_row(string_number, 2, str(self.disk.get_devices_space().get(disk).get("total")))
            self.draw_disk_info_row(string_number, 3, str(self.disk.get_devices_space().get(disk).get("used")))
            self.draw_disk_info_row(string_number, 4, str(self.disk.get_devices_space().get(disk).get("free")))
            self.draw_disk_info_row(string_number, 5, str(self.disk.get_devices_space().get(disk).get("percent")))
            string_number += 1
