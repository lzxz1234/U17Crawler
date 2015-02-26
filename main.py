# -*- coding: utf-8 -*-

import sys

from ui.MainWindow import Ui_MainWindow
from ui.Model import ComicProcessModel
from PyQt4 import QtGui
from PyQt4 import Qt
from PyQt4 import QtCore

reload(sys)
sys.setdefaultencoding('utf8')

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.contextMenu = QtGui.QMenu(self)
        self.c_menu_export = self.contextMenu.addAction(u'导出')

        self.button_reset.connect(self.button_reset,
                                  Qt.SIGNAL("clicked()"),
                                  lambda : self.input_book_name.setText(''))
        self.button_query.connect(self.button_query,
                                  Qt.SIGNAL("clicked()"),
                                  lambda : self.treeView.setModel(ComicProcessModel(self.input_book_name.text())))
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.treeView,
                     Qt.SIGNAL("customContextMenuRequested(QPoint)"),
                     self.showContextMenu)

    def showContextMenu(self, point):
        self.contextMenu.move(self.pos()+self.menubar.pos()+self.centralwidget.pos() + point)
        self.contextMenu.show()

    def export(self):
        print(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())