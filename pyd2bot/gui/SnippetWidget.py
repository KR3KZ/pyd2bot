import os
import uuid

import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QComboBox

from core import env


class QSnip(QMainWindow):

    snippetTaken = pyqtSignal(list)
    captureModeExited = pyqtSignal()

    def __init__(self, parent, snip_types):
        super(QSnip, self).__init__()
        self.parent = parent
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.5)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.showMaximized()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()
        self.capturing = False
        self.snip_types = snip_types

    def paintEvent(self, event):
        brush_color = (255, 128, 255, 128)
        thickness = 1
        opacity = 0.3
        color = 'red'
        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor(color), thickness, QtCore.Qt.DotLine))
        qp.setBrush(QtGui.QColor(*brush_color))
        for entry in self.parent.path_list.getMapList(self.parent.curr_map_idx):
            rec = list(map(int, entry[1:-1]))
            qp.drawRect(QtCore.QRect(*rec))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.QApplication.restoreOverrideCursor()
            self.close()
            self.captureModeExited.emit()
        event.accept()

    def mousePressEvent(self, event):
        self.capturing = True
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        if self.capturing:
            self.end = event.pos()
            self.update()

    def madeChoice(self, capture_type):
        self.captureType = capture_type
        if capture_type != 'mapChange':
            QtCore.QTimer.singleShot(1 * 1000, self.saveShot)
            self.hide()
        else:
            rec = QtCore.QRect(self.begin, self.end)
            capture = [self.captureType, rec.x(), rec.y(), rec.width(), rec.height(), 'None']
            self.snippetTaken.emit(capture)

    def saveShot(self):
        rec = QtCore.QRect(self.begin, self.end)
        capture = [self.captureType, rec.x(), rec.y(), rec.width(), rec.height(), 'None']

        bi = env.capture(rec)
        image_id = str(uuid.uuid4().hex)
        image_file = os.path.join(self.parent.patternDir(self.captureType), image_id + ".png")
        cv2.imwrite(image_file, bi)
        capture[-1] = image_id
        self.snippetTaken.emit(capture)
        self.show()

    def mouseReleaseEvent(self, event):
        self.capturing = False
        combo_box = QComboBox(self)
        for st in self.snip_types:
            combo_box.addItem(st)
        combo_box.move(self.end.x(), self.end.y())
        combo_box.activated[str].connect(self.madeChoice)
        combo_box.showPopup()
