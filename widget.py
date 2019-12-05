import datetime
import sys

from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from full_info import *
from PyQt5.QtWidgets import *


class tabdemo(QTabWidget):
    def __init__(self):
        super().__init__()
        self.info = GetInfo()

        self.resize(1000, 900)
        self.tab1 = QWidget()
        self.setStyleSheet("font-size: 18px;")

        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.time_label = QLabel(info.get_time().get("Uptime"))

        self.addTab(self.tab1, "Disk Info")
        self.addTab(self.tab2, "BIOS Info")
        self.addTab(self.tab3, "CPU Info")
        self.addTab(self.tab4, "Board Info")
        self.addTab(self.tab5, "Time Info")

        self.show_tabs()
        self.show_time()
        self.setWindowTitle("tab demo")

    def show_tabs(self):
        self.grid_layout = QGridLayout()
        self.tab1.setLayout(self.grid_layout)
        self.grid_layout.setSpacing(0)
        self.show_disk_table_headers(self.grid_layout)
        self.show_disk_form(self.grid_layout)

        self.draw_tab_layout(self.info.get_bios_info().items())
        self.tab2.setLayout(self.horizontallayout)
        self.draw_tab_layout(self.info.get_cpu_info().items())
        self.tab3.setLayout(self.horizontallayout)
        self.draw_tab_layout(self.info.get_board_info().items())
        self.tab4.setLayout(self.horizontallayout)

        # self.draw_tab_layout(self.info.get_time().items())
        # self.tab5.setLayout(self.horizontallayout)

    def draw_tab_layout(self, data):
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        for k, v in data:
            label = QLabel(k)
            label.setStyleSheet("max-height: 20px; font-size: 17px;")
            self.verticalLayout.addWidget(label)
            label_2 = QLabel(v)
            label_2.setStyleSheet("max-height: 20px; font-size: 17px;")
            self.verticalLayout_2.addWidget(label_2)
        last_label = QLabel()
        self.verticalLayout.addWidget(last_label)
        self.verticalLayout_2.addWidget(last_label)
        self.horizontallayout = QHBoxLayout()
        self.horizontallayout.addLayout(self.verticalLayout)
        self.horizontallayout.addLayout(self.verticalLayout_2)
        self.horizontallayout.setSpacing(1)
        self.tab4.setLayout(self.horizontallayout)

    def show_time(self):
        self.verticalLayout = QVBoxLayout()
        self.label = QLabel("Curent Ttime")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.current_time_label = QLabel(str(datetime.datetime.today()))
        self.verticalLayout.addWidget(self.current_time_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label = QLabel("Curent Uptime")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.time_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.tab5.setLayout(self.verticalLayout)

    def update_time(self):
        self.time_label.setText(self.info.get_time().get("Uptime"))
        self.current_time_label.setText(str(datetime.datetime.today()))

    def show_disk_table_headers(self, layout):
        headers = ["Total", "Used", "Free", "Percent", "File System"]
        position = 2
        for header in headers:
            title = QLabel(header)
            title.setStyleSheet("font-size:18px; max-height: 30px")
            layout.addWidget(title, 0, position)
            position += 1

    def draw_disk_info_row(self, position_x, position_y, value, layout):
        text_edit = QTextEdit(value)
        text_edit.setStyleSheet("font-size: 17px; max-height: 30px;")
        layout.addWidget(text_edit, position_x, position_y)

    def show_disk_form(self, layout):
        string_number = 1
        for disk in self.info.get_all_devices():
            label = QLabel(disk)
            label.setStyleSheet("font-size: 20px;")
            layout.addWidget(label, string_number, 1)
            self.draw_disk_info_row(string_number, 2, str(self.info.get_devices_space().get(disk).get("total")), layout)
            self.draw_disk_info_row(string_number, 3, str(self.info.get_devices_space().get(disk).get("used")), layout)
            self.draw_disk_info_row(string_number, 4, str(self.info.get_devices_space().get(disk).get("free")), layout)
            self.draw_disk_info_row(string_number, 5, str(self.info.get_devices_space().get(disk).get("percent")), layout)
            self.draw_disk_info_row(string_number, 6, str(self.info.get_devices_file_system().get(disk)), layout)
            string_number += 1


def main():
    app = QApplication(sys.argv)
    ex = tabdemo()
    ex.show()
    timer = QTimer()
    timer.timeout.connect(ex.update_time)
    timer.start(100)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
