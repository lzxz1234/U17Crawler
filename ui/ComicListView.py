# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, Qt
from ui.Model import ComicItem, ChapterItem, ImageItem
from util.ThreadPool import ThreadPool
from core.PDF import Generator

class ComicListView(QtGui.QTreeView):

    def __init__(self, parent = None):
        super(ComicListView, self).__init__(parent)
        self.thread_pool = ThreadPool(1)
        self.contextMenu = QtGui.QMenu(self)
        self.c_menu_export = self.contextMenu.addAction(u'导出')
        self.c_menu_export.connect(self.c_menu_export,
                                   Qt.SIGNAL("triggered()"),
                                   self.export)

    def contextMenuEvent(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return
        self.current_item = index.internalPointer()

        self.contextMenu.move(event.globalPos())
        self.contextMenu.show()

    def export(self):
        if isinstance(self.current_item, ComicItem):
            self.export_comic(self.current_item)
        elif isinstance(self.current_item, ChapterItem):
            self.export_chapters((self.current_item, ))
        elif isinstance(self.current_item, ImageItem):
            self.export_images((self.current_item, ))

    def export_comic(self, comic):
        self.export_chapters(comic.get_children())

    def export_chapters(self, chapters):
        images = []
        for chapter in chapters:
            images.extend(chapter.get_children())
        self.export_images(images)

    def export_images(self, images):
        dialog = QtGui.QFileDialog()
        save_path = unicode(dialog.getSaveFileName())
        self.thread_pool.add_task(lambda: Generator().gen_from_files(save_path, images))