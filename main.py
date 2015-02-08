# -*- coding: utf-8 -*-

import sys

from ui.MainWindow import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4 import Qt

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.button_reset.connect(self.button_reset,
                                  Qt.SIGNAL("clicked()"),
                                  lambda : self.input_book_name.setText(''))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())