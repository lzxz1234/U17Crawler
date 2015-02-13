# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import Qt
from core.Crawler import Fetcher


class ComicProcessModel(QtCore.QAbstractItemModel):

    def __init__(self, query_name):
        super(ComicProcessModel, self).__init__()
        self._root_item = RootItem(str(query_name))
        self.connect(self,
                     Qt.SIGNAL("customContextMenuRequested(QPoint)"),
                     self.rightClick)

    def rightClick(self, point):
        print(point)

    def index(self, row, column, parent_index=None, *args, **kwargs):
        if not self.hasIndex(row, column, parent_index):
            return QtCore.QModelIndex()

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
        if parent_item == self._root_item:
            return QtCore.QModelIndex()
        return self.createIndex(parent_item.row(), 0, parent_item)

    def rowCount(self, parent_index=QtCore.QModelIndex(), *args, **kwargs):
        if parent_index.column() > 0:
            return 0

        if not parent_index.isValid():
            item = self._root_item
        else:
            item = parent_index.internalPointer()
        return item.get_child_count()

    def columnCount(self, parent_index=QtCore.QModelIndex(), *args, **kwargs):
        if not parent_index.isValid():
            return self._root_item.column_count()
        return parent_index.internalPointer().column_count()

    def data(self, index, role=None):
        if not index.isValid():
            return QtCore.QVariant()

        item = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            return item.get_name()
        if role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(50,50)
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignVCenter
        return QtCore.QVariant()

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):
            try:
                return self._root_item.column(column)
            except IndexError:
                pass
        return QtCore.QVariant()

class BaseItem():

    def __init__(self, parent):
        self._fetcher = Fetcher()
        self._parent = parent
        self._name = None
        self._children = []
        self._columns = []

    def column_count(self):
        return 1

    def column(self, index):
        return self._columns[index]

    def get_child(self, row):
        return self._children[row]

    def get_children(self):
        return self._children

    def get_child_count(self):
        if len(self._children) == 0:
            self.load()
        return len(self._children)

    def add_child(self, child):
        self._children.append(child)

    def get_parent(self):
        return self._parent

    def get_name(self):
        return self._name

    def row(self):
        if self._parent:
            return self._parent._children.index(self)
        return 0

    def load(self):
        pass

class RootItem(BaseItem):

    def __init__(self, book_name, parent = None):
        BaseItem.__init__(self, parent)
        self._columns = [u'名称']
        self._book_name = book_name

    def load(self):
        for c_name, c_url in self._fetcher.queryComic(self._book_name):
            self.add_child(ComicItem(c_name, c_url, self))

class ComicItem(BaseItem):

    def __init__(self, c_name, c_url, parent):
        BaseItem.__init__(self, parent)
        self._name = c_name
        self._c_url = c_url

    def load(self):
        for ch_name, ch_url in self._fetcher.queryChapters(self._c_url):
            self.add_child(ChapterItem(ch_name, ch_url, self))

class ChapterItem(BaseItem):

    def __init__(self, ch_name, ch_url, parent):
        BaseItem.__init__(self, parent)
        self._name = ch_name
        self._ch_url = ch_url

    def load(self):
        for img_url in self._fetcher.queryImages(self._ch_url):
            self.add_child(ImageItem(img_url, self))

class ImageItem(BaseItem):

    def __init__(self, url, parent):
        BaseItem.__init__(self, parent)
        self._url = url
        self._name = url