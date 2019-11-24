import sys
from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from hdd_info import DiskInfo


class tabdemo(QTabWidget):
    def __init__(self):
        super().__init__()
        self.resize(693, 478)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.disk = DiskInfo()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("tab demo")

    # def tab1UI(self):
    #     layout = QFormLayout()
    #     layout.addRow("Name", QLineEdit())
    #     layout.addRow("Address", QLineEdit())
    #     self.setTabText(0, "Contact Details")
    #     self.tab1.setLayout(layout)

    def tab1UI(self):
        grid_layout = QGridLayout()
        self.setTabText(0, "Disk Info")
        self.tab1.setLayout(grid_layout)
        grid_layout.setSpacing(0)
        grid_layout.setObjectName("gridLayout")
        self.show_disk_table_headers(grid_layout)
        self.show_disk_form(grid_layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())
        self.setTabText(1, "Personal Details")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.setTabText(2, "Education Details")
        self.tab3.setLayout(layout)

    def show_disk_table_headers(self, layout):
        headers = ["Total", "Used", "Free", "Percent"]
        position = 2
        for header in headers:
            title = QLabel(self)
            title.setStyleSheet("font-size:18px; max-height: 30px")
            title.setText(header)
            title.setObjectName("header")
            layout.addWidget(title, 0, position)
            position += 1

    def draw_disk_info_row(self, position_x, position_y, value, layout):
        text_edit = QTextEdit()
        text_edit.setStyleSheet("font-size: 17px; max-height: 30px;")
        text_edit.setObjectName("text_edit")
        layout.addWidget(text_edit, position_x, position_y)
        text_edit.setText(value)

    def show_disk_form(self, layout):
        string_number = 1
        for disk in self.disk.get_all_devices():
            label = QLabel(self)
            label.setStyleSheet("font-size: 20px;")
            label.setObjectName("label")
            layout.addWidget(label, string_number, 1)
            label.setText(disk)
            self.draw_disk_info_row(string_number, 2, str(self.disk.get_devices_space().get(disk).get("total")), layout)
            self.draw_disk_info_row(string_number, 3, str(self.disk.get_devices_space().get(disk).get("used")), layout)
            self.draw_disk_info_row(string_number, 4, str(self.disk.get_devices_space().get(disk).get("free")), layout)
            self.draw_disk_info_row(string_number, 5, str(self.disk.get_devices_space().get(disk).get("percent")), layout)

            string_number += 1


def main():
    app = QApplication(sys.argv)
    ex = tabdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
