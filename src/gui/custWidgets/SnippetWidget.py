import os
import uuid
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QComboBox

from core import env


class QSnip(QMainWindow):

    snippetTaken = pyqtSignal(list)
    captureModeExited = pyqtSignal()

    def __init__(self, parent, patterns_dir):
        super(QSnip, self).__init__()
        self.parent = parent
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.5)
        self.capturing = False
        self.patterns_dir = patterns_dir
        self.selected = []
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.showMaximized()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        brush_color = (255, 128, 255, 128)
        thickness = 1
        opacity = 0.3
        color = 'red'
        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor(color), thickness, QtCore.Qt.DotLine))
        qp.setBrush(QtGui.QColor(*brush_color))
        for r in self.selected:
            qp.drawRect(r)
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.QApplication.restoreOverrideCursor()
            self.hide()
            QtCore.QTimer.singleShot(1 * 1000, self.saveShots)
        event.accept()

    def saveShots(self):
        for r in self.selected:
            bi = env.capture(r)
            image_file = os.path.join(self.patterns_dir, str(uuid.uuid4().hex) + ".png")
            cv2.imwrite(image_file, bi)
        self.close()
        self.captureModeExited.emit()

    def mousePressEvent(self, event):
        self.capturing = True
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        if self.capturing:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.capturing = False
        self.selected.append(QRect(self.begin, self.end))


