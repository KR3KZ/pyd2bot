from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton, QAction
import tkinter as tk


class QSnip(QMainWindow):

    def __init__(self, parent):
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
        self.takeSnipEnded = pyqtSignal()
        self.parent.hide()
        self.show()

    def paintEvent(self, event):
        # capture rectangle style
        brush_color = (128, 128, 255, 128)
        thickness = 0
        opacity = 0.3
        color = 'black'
        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor(color), thickness))
        qp.setBrush(QtGui.QColor(*brush_color))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.QApplication.restoreOverrideCursor()
            self.close()
        event.accept()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def madeChoice(self, value):
        QtWidgets.QApplication.restoreOverrideCursor()
        self.takeSnipEnded.emit()
        self.parent.show()
        self.close()

    def mouseReleaseEvent(self, event):
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        self.repaint()
        QtWidgets.QApplication.processEvents()
        self.repaint()
        QtWidgets.QApplication.processEvents()
        combo_box = QComboBox(self)
        combo_box.addItem("mapChange")
        combo_box.addItem("kralamoure")
        combo_box.addItem("poisskaille")
        combo_box.addItem("poissonPane")
        combo_box.addItem("sardineBrillante")
        combo_box.move(self.end.x(), self.end.y())
        combo_box.activated[str].connect(self.madeChoice)
        combo_box.showPopup()
