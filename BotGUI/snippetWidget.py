from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton, QAction
import tkinter as tk


class QSnip(QMainWindow):

    snippetTaken = pyqtSignal(list)
    captureModeExited = pyqtSignal()

    def __init__(self, parent, snip_types):
        super(QSnip, self).__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.parent = parent
        self.setGeometry(0, 0, screen_width, screen_height)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
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
            rec = map(int, entry[1:])
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
        rec = QtCore.QRect(self.begin, self.end)
        capture = [capture_type, rec.x(), rec.y(), rec.width(), rec.height()]
        self.snippetTaken.emit(capture)

    def mouseReleaseEvent(self, event):
        self.capturing = False
        combo_box = QComboBox(self)
        for st in self.snip_types:
            combo_box.addItem(st)
        combo_box.move(self.end.x(), self.end.y())
        combo_box.activated[str].connect(self.madeChoice)
        combo_box.showPopup()
