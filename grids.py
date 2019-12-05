# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grids.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QTextEdit {""height: 30px;""}")
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 321, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 1, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 112))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(29, 19, 231, 201))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 191, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_5 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_5.setStyleSheet("max-height: 30px;  max-width: 159px;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_2.addWidget(self.textEdit_5, 0, 0, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_2.addWidget(self.textEdit_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))


class Example(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Example()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
