import os
import sys
import dropbox
import datetime
from full_info import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabwidget = QTabWidget()
        self.resize(1000, 900)
        self.tab1 = QWidget()
        self.setStyleSheet("font-size: 18px;")
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.uptime_time_label = QLabel()
        self.tabwidget.addTab(self.tab1, "Disk Info")
        self.tabwidget.addTab(self.tab2, "BIOS Info")
        self.tabwidget.addTab(self.tab3, "CPU Info")
        self.tabwidget.addTab(self.tab4, "Board Info")
        self.tabwidget.addTab(self.tab5, "Time Info")
        self.show_tabs()
        self.show_time()
        self.show_tool_bar()
        self.setWindowTitle("Spo Project")
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setCentralWidget(self.tabwidget)

    def on_download_click(self):
        with open("report.txt", "w") as file:
            for i in create_report():
                file.write(i)

    def on_upload_click(self):
        self.on_download_click()
        access_token = 'qdk5zENbrdAAAAAAAAAAFvnjG-29PQguW8DRsghUQJFT5t9o5_6lcXPquzqcePtU'
        file_from = 'report.txt'  # local file path
        file_to = f'/spo_project/{datetime.datetime.now()}report.txt'  # dropbox path
        dbx = dropbox.Dropbox(access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        # Ссыдка на файлы
        # https://www.dropbox.com/sh/rovxw54epmu6pp4/AADD4fe28-j58p6NswVWOM9ia?dl=0

    def show_tool_bar(self):
        exitAction = QAction(QIcon("images/exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)
        download_report = QAction(QIcon("images/download.png"), "Download report", self)
        download_report.setShortcut("Ctrl+D")
        download_report.triggered.connect(self.on_download_click)
        upload_report = QAction(QIcon("images/upload.png"), "Download report", self)
        upload_report.setShortcut("Ctrl+D")
        upload_report.triggered.connect(self.on_upload_click)
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(download_report)
        self.toolbar.addAction(upload_report)

    def show_tabs(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.tab1.setLayout(self.grid_layout)
        self.show_disk_table_headers(self.grid_layout)
        self.show_disk_form(self.grid_layout)
        self.draw_tab_layout(get_bios_info().items())
        self.tab2.setLayout(self.horizontallayout)
        self.draw_tab_layout(get_cpu_info().items())
        self.tab3.setLayout(self.horizontallayout)
        self.draw_tab_layout(get_board_info().items())
        self.tab4.setLayout(self.horizontallayout)

    def draw_tab_layout(self, data):
        self.verticallayout = QVBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        for k, v in data:
            label = QLabel(k)
            label.setStyleSheet("max-height: 20px; font-size: 17px;")
            self.verticallayout.addWidget(label)
            label_2 = QLabel(v)
            label_2.setStyleSheet("max-height: 20px; font-size: 17px;")
            self.verticalLayout_2.addWidget(label_2)
        last_label = QLabel()
        self.verticallayout.addWidget(last_label)
        self.verticalLayout_2.addWidget(last_label)
        self.horizontallayout = QHBoxLayout()
        self.horizontallayout.addLayout(self.verticallayout)
        self.horizontallayout.addLayout(self.verticalLayout_2)
        self.horizontallayout.setSpacing(1)
        self.tab4.setLayout(self.horizontallayout)

    def show_time(self):
        self.layout = QVBoxLayout()
        self.label_2 = QLabel("Current Uptime")
        self.layout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.uptime_time_label, 0, QtCore.Qt.AlignHCenter)
        self.uptime_time_label.setStyleSheet("max-height: 45px; font-size: 40px; margin-bottom: 40px;")
        self.label_2.setStyleSheet("max-height: 25px; margin-top: 20px;")
        self.label = QLabel("Current Time")
        self.label.setStyleSheet("max-height: 25px;")
        self.layout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.current_time_label = QLabel(str(datetime.datetime.today()))
        self.current_time_label.setStyleSheet("max-height: 45px; font-size: 40px; margin-bottom: 40px;")
        self.layout.addWidget(self.current_time_label, 0, QtCore.Qt.AlignHCenter)
        self.label_1 = QLabel("Last BootTime")
        self.label_1.setStyleSheet("max-height: 25px;")
        self.layout.addWidget(self.label_1, 0, QtCore.Qt.AlignHCenter)
        self.boot_time_label = QLabel(get_time().get("BootTime"))
        self.boot_time_label.setStyleSheet("max-height: 45px; font-size: 40px; margin-bottom: 40px;")
        self.layout.addWidget(self.boot_time_label, 0, QtCore.Qt.AlignHCenter)
        self.last_label = QLabel()
        self.layout.addWidget(self.last_label)
        self.tab5.setLayout(self.layout)

    def update_time(self):
        self.uptime_time_label.setText(get_time().get("Uptime"))
        self.current_time_label.setText(str(datetime.datetime.today()))

    def show_disk_table_headers(self, layout):
        headers = ["Total", "Used", "Free", "Percent", "File System"]
        position = 2
        for header in headers:
            title = QLabel(header)
            title.setStyleSheet("font-size:18px; max-height: 30px;")
            layout.addWidget(title, 0, position)
            position += 1

    def draw_disk_info_row(self, position_x, position_y, value, layout):
        text_edit = QTextEdit(value)
        text_edit.setStyleSheet("font-size: 17px; max-height: 30px;")
        layout.addWidget(text_edit, position_x, position_y)

    def show_disk_form(self, layout):
        string_number = 1
        for disk in get_all_devices():
            label = QLabel(disk)
            label.setStyleSheet("font-size: 20px; max-height: 30px;")
            layout.addWidget(label, string_number, 1)
            self.draw_disk_info_row(string_number, 2, str(get_devices_space().get(disk).get("total")), layout)
            self.draw_disk_info_row(string_number, 3, str(get_devices_space().get(disk).get("used")), layout)
            self.draw_disk_info_row(string_number, 4, str(get_devices_space().get(disk).get("free")), layout)
            self.draw_disk_info_row(string_number, 5, str(get_devices_space().get(disk).get("percent")), layout)
            self.draw_disk_info_row(string_number, 6, str(get_devices_file_system().get(disk)), layout)
            string_number += 1
        last_label = QLabel()
        layout.addWidget(last_label, string_number, 1)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    timer = QTimer()
    timer.timeout.connect(ex.update_time)
    timer.start(100)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()