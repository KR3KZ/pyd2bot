from time import sleep, perf_counter
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QColor, QPainter, QPolygon, QPen, QBrush, QPolygonF
from PyQt5.QtCore import QRect, QPointF, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication


class Overlay(QMainWindow):
    highlightEnded = pyqtSignal()

    def __init__(self, parent=None):
        super(Overlay, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.target_color = QColor(1, 0, 0, 0.7)

    def onHighlightEnded(self):
        self.highlightEnded.emit()
        self.close()

    def closeAfter(self, secs):
        timer = QtCore.QTimer(self)
        timer.setInterval(secs * 1000)
        timer.timeout.connect(self.onHighlightEnded)
        timer.start()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine))
        qp.drawRect(QRect(0, 0, self.width(), self.height()))

    def highlight(self, r, secs):
        self.setGeometry(*r.getRect())
        self.show()
        if secs:
            self.closeAfter(secs)


class CellOverlay(Overlay):
    class VizMode:
        Border = 1
        Ellipse = 2
        Fill = 3
        Shape = 4

    def __init__(self, cell, mode=VizMode.Border, parent=None):
        super(CellOverlay, self).__init__(parent)
        self.cell = cell
        self.mode = mode
        self.shape = None
        self.setGeometry(int(self.cell.x - self.cell.w / 2), int(self.cell.y - self.cell.h / 2), int(self.cell.w),
                         int(self.cell.h))

    def drawEllipse(self):
        thickness = 3
        color = self.cell.type
        qp = QPainter(self)
        qp.setPen(QtGui.QPen(QColor(color), thickness, QtCore.Qt.SolidLine))
        w = self.cell.extEllipse[0] * self.cell.w / 2
        h = self.cell.extEllipse[1] * self.cell.h / 2
        x = int((self.cell.w - w) / 2)
        y = int((self.cell.h - h) / 2)
        qp.drawEllipse(x, y, int(w), int(h))

    def drawBorder(self):
        qp = QPainter(self)
        qp.setPen(QtGui.QPen(QColor(self.cell.type), 3, QtCore.Qt.SolidLine))
        edges = QPolygon(QPointF(self.cell.w / 2, 0),
                         QPointF(self.cell.w, self.cell.h / 2),
                         QPointF(self.cell.w / 2, self.cell.h),
                         QPointF(0, self.cell.h / 2))
        qp.drawPolygon(edges)

    def drawShape(self):
        pen = QtGui.QPen(Qt.green, 3, QtCore.Qt.SolidLine)
        qp = QPainter(self)
        qp.setPen(pen)
        for point in self.shape:
            x = int(point.x() - self.cell.x + self.cell.w / 2)
            y = int(point.y() - self.cell.y + self.cell.h / 2)
            qp.drawPoint(x, y)

    def paintEvent(self, event):
        if self.mode == CellOverlay.VizMode.Border:
            self.drawBorder()
        elif self.mode == CellOverlay.VizMode.Ellipse:
            self.drawEllipse()
        elif self.mode == CellOverlay.VizMode.Shape:
            self.drawShape()

    def highlight(self, secs, mode=None, shape=None):
        if mode == CellOverlay.VizMode.Shape and not shape:
            raise Exception("A shape of points must be specified in Shape mode!")
        if mode:
            self.mode = mode
        if shape:
            self.shape = shape
        self.show()
        if secs:
            self.closeAfter(secs)


class GridOverlay(Overlay):

    def __init__(self, grid, parent=None):
        super(GridOverlay, self).__init__(parent)
        self.grid = grid
        self.setGeometry(self.grid.x(), self.grid.y(), self.grid.width(), self.grid.height())

    def paintEvent(self, event):
        qp = QPainter(self)
        pen = QPen(QColor(255, 0, 0), 1, QtCore.Qt.SolidLine)
        brush = QBrush(QColor(255, 0, 0))
        qp.setPen(pen)
        for cell in self.grid:
            pen.setColor(cell.type)
            brush_color = QColor(cell.type)
            brush.setColor(brush_color)
            qp.setPen(pen)
            qp.setBrush(brush)
            edges = [QPointF(cell.x - self.grid.x(), cell.y - self.grid.y() + cell.h / 2),
                     QPointF(cell.x - self.grid.x() + cell.w / 2, cell.y - self.grid.y()),
                     QPointF(cell.x - self.grid.x(), cell.y - self.grid.y() - cell.h / 2),
                     QPointF(cell.x - self.grid.x() - cell.w / 2, cell.y - self.grid.y())]
            edges = QPolygonF(edges)
            qp.drawPolygon(edges)

    def highlight(self, secs):
        self.show()
        if secs:
            self.closeAfter(secs)


def window():
    from core.grid import Grid as G
    import json
    app = QApplication(sys.argv)
    sleep(2)
    grid = G(env.COMBAT_R, env.VCELLS, env.HCELLS)
    start = perf_counter()
    grid.parse()
    print("it took: ", perf_counter() - start)
    # grid.fromJson("map.json")
    # win = GridOverlay(grid)
    # win.highlight(10)
    grid.highlight(5)
    sys.exit(app.exec_())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
    from core import env

    sys.excepthook = except_hook
    window()
