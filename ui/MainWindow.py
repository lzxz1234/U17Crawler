# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Workspaces\Python\U17Crawler\ui\MainWindow.ui'
#
# Created: Thu Feb 26 18:17:23 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(766, 563)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.input_book_name = QtGui.QLineEdit(self.centralwidget)
        self.input_book_name.setObjectName(_fromUtf8("input_book_name"))
        self.gridLayout.addWidget(self.input_book_name, 0, 0, 1, 1)
        self.button_query = QtGui.QPushButton(self.centralwidget)
        self.button_query.setObjectName(_fromUtf8("button_query"))
        self.gridLayout.addWidget(self.button_query, 0, 1, 1, 1)
        self.button_reset = QtGui.QPushButton(self.centralwidget)
        self.button_reset.setObjectName(_fromUtf8("button_reset"))
        self.gridLayout.addWidget(self.button_reset, 0, 2, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_about = QtGui.QMenu(self.menubar)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_lzxz1234 = QtGui.QAction(MainWindow)
        self.action_lzxz1234.setObjectName(_fromUtf8("action_lzxz1234"))
        self.menu_file.addAction(self.action_exit)
        self.menu_about.addAction(self.action_lzxz1234)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_query.setText(_translate("MainWindow", "搜索", None))
        self.button_reset.setText(_translate("MainWindow", "重置", None))
        self.menu_file.setTitle(_translate("MainWindow", "文件", None))
        self.menu_about.setTitle(_translate("MainWindow", "关于", None))
        self.action_exit.setText(_translate("MainWindow", "退出", None))
        self.action_lzxz1234.setText(_translate("MainWindow", "lzxz1234", None))

