from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal, QObject, QPoint, QRect
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLabel, QPushButton, QAction
import traceback
import logging
from math import sqrt
from time import sleep


class Overlay(QMainWindow):

    def __init__(self):
        super(Overlay, self).__init__()
        self.setWindowOpacity(0.0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.target_color = QColor(1, 0, 0, 0.7)

    def closeAfter(self, secs):
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(secs * 1000)
        self.timer.timeout.connect(self.close)
        self.timer.start()

    def paint(self, g):
        super(Overlay, self).paint(g)
        stroke = BasicStroke(3)
        g.setColor(self.target_color)
        g.setStroke(stroke)
        w = stroke.getLineWidth()
        g.drawRect(int(w / 2), int(w / 2), int(self.getWidth() - w), int(self.getHeight() - w))

    def highlight(self, r, secs):
        self.setGeometry(r)
        self.show()
        if secs:
            self.closeAfter(secs)
