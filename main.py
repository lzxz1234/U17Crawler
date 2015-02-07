# -*- coding: utf-8 -*-

import sys

from ui.MainWindow import Ui_MainWindow
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())