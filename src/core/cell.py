import sys
from math import sqrt

import pyautogui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

from core.env import ObjColor, ObjType
from core.utils import iterParallelogram
from gui.Overlay import CellOverlay
from core.log import Log

log = Log()


class Cell:

    def __init__(self, pgrid, x, y, i, j, ctype=ObjType.UNKNOWN):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.grid = pgrid
        self.h = pgrid.cell_h
        self.w = pgrid.cell_w
        self.extEllipse = (0.55, 0.6)
        self.type = ctype
        self.rx, self.ry = self.x - self.grid.x(), self.y - self.grid.y()

    def __iter__(self):
        return iterParallelogram(self, self.w, self.h)

    def __contains__(self, loc):
        res = self.w * abs(loc.y()) + self.h * (abs(loc.x()) - self.w / 2) <= 0
        return res

    def iterEllipse(self, thickness=2):
        a = self.extEllipse[0] * self.w / 2
        b = self.extEllipse[1] * self.h / 2
        for dx in range(int(a) + 1):
            dy = int(b * sqrt(1 - (dx / a) ** 2))
            for eps in range(thickness):
                yield QPoint(self.x + dx, self.y + dy - eps)
                yield QPoint(self.x + dx, self.y - dy - eps)
                yield QPoint(self.x - dx, self.y + dy - eps)
                yield QPoint(self.x - dx, self.y - dy - eps)

    def getpixel(self, p):
        return self.grid.getpixel(p)

    def dist(self, cell):
        i = abs(self.x() - cell.x()) / self.w
        j = abs(self.y() - cell.y()) / self.h
        return max(int(i), int(j))

    def distx(self, cell):
        j = (self.x() - cell.x()) / self.w
        return int(j)

    def parse(self):
        hist = {}
        max_key = None
        max_val = 0

        unknown = set()

        for loc in self.iterTopCorner():
            rgb = self.getpixel(loc).getRgb()
            if rgb not in hist:
                hist[rgb] = 0
            hist[rgb] += 1
            if hist[rgb] > max_val:
                max_val = hist[rgb]
                max_key = rgb
            if max_val > 5:
                break

        max_key = QColor(*max_key)

        if max_key in ObjColor.OBSTACLE:
            self.type = ObjType.OBSTACLE

        elif max_key in ObjColor.FREE:
            self.type = ObjType.FREE

        elif max_key in ObjColor.REACHABLE:
            self.type = ObjType.REACHABLE

        elif max_key in ObjColor.INVOKE:
            self.type = ObjType.INVOKE

        elif max_key in ObjColor.MOB:
            self.type = ObjType.MOB

        elif max_key in ObjColor.BOT:
            self.type = ObjType.BOT

        else:
            if max_key.getRgb() not in unknown:
                log.info("Unknown color: ", max_key.getRgb())
                unknown.add(max_key.getRgb())
            self.type = max_key

        return self.type

    def iterTopCorner(self):
        a = 0.4
        b = 0.5
        c = 0.7
        o = QPoint(self.x, self.y - (self.h / 4) * (b + c))
        w = a * self.w / 2
        h = b * self.h / 2
        return iterParallelogram(o, w, h)

    def highlight(self, secs, mode=CellOverlay.VizMode.Border):
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode)

    def highlightTopCorner(self, secs):
        sys.excepthook = except_hook
        app = QApplication(sys.argv)
        top_corner_it = self.iterTopCorner()
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode=CellOverlay.VizMode.Shape, shape=top_corner_it)
        sys.exit(app.exec_())

    def click(self):
        pyautogui.click(self.x, self.y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)