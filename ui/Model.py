# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from core.Crawler import Fetcher


class ComicProcessModel(QtCore.QAbstractItemModel):

    def __init__(self, query_name):
        super(ComicProcessModel, self).__init__()
        self._query_name = str(query_name)
        self._headers = [u'序号', u'书名']
        self._root_item = ComicItem(self._query_name)

    def index(self, row, column, parent_index=None, *args, **kwargs):

        if not self.hasIndex(row, column, parent_index):
            return QtCore.QModelIndex()

        parent_item = None
        if not parent_index.isValid():
            parent_item = self._root_item
        else:
            parent_item = parent_index.internalPointer()

        child_item = parent_item.get_child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        else:
            return QtCore.QModelIndex()

    def parent(self, child_index=None):
        if not child_index.isValid():
            return QtCore.QModelIndex()

        child_item = child_index.internalPointer()
        if not child_item:
            return QtCore.QModelIndex()

        parent_item = child_item.get_parent()
        if parent_item == self.rootItem:
            return QtCore.QModelIndex()
        return self.createIndex(parent_item.Row(), 0, parent_item)


    def rowCount(self, index=QtCore.QModelIndex(), *args, **kwargs):
        return len(self._comic_list)

    def columnCount(self, index=QtCore.QModelIndex(), *args, **kwargs):
        return 2

    def data(self, index, role=None):
        row, col = index.row(), index.column()
        if not index.isValid():
            return QtCore.QVariant()

        if role == QtCore.Qt.TextAlignmentRole:
            if col == 0:
                return QtCore.Qt.AlignVCenter
            else:
                return QtCore.Qt.AlignLeft
        elif role == QtCore.Qt.DisplayRole:
            if col == 0:
                return QtCore.QString(str(row + 1))
            elif col == 1:
                return QtCore.QVariant(self._comic_list[row][0])
        elif role == QtCore.Qt.ToolTipRole:
            if col == 1:
                return QtCore.QVariant(self._comic_list[row][1])

        return QtCore.QVariant()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self._headers[section]

class BaseItem():

    def __init__(self, parent):
        self._fetcher = Fetcher()
        self._parent = parent
        self._children = []

    def get_child(self, row):
        return self._children[row]

    def add_child(self, child):
        self._children.append(child)

    def get_child_count(self):
        return len(self._children)

    def get_parent(self):
        return None

class ComicItem(BaseItem):

    def __init__(self, parent, book_name):
        BaseItem.__init__(self, parent)
        self._comic_list = self._fetcher.queryComic(book_name)