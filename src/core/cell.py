import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from core import dofus, env
from core.dofus import ObjColor, ObjType
from core.region import Region
from core.utils import iterParallelogram
from gui.Overlay import CellOverlay
from core.log import Log


class ParseFailed(Exception):
    pass


log = Log()


class Cell:

    def __init__(self, pgrid, x, y, i, j, ctype=ObjType.UNKNOWN):
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.w = pgrid.cell_w
        self.h = pgrid.cell_h
        self.grid = pgrid
        self.extEllipse = (0.55, 0.6)
        self.type = ctype
        self.rx, self.ry = self.x - self.grid.x(), self.y - self.grid.y()
        self.dotted = False
        self._r = Region(self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)

    def getpixel(self, x, y, from_grid=True):
        rx = x - self.grid.x()
        ry = y - self.grid.y()
        if from_grid:
            return self.grid.getpixel(rx, ry)
        else:
            return self._r.getpixel(x - self._r.x(), y - self._r.y())

    def parse(self, from_grid=True):
        hist = {}
        max_key = (0, 0, 0)
        max_val = 0
        unknown = set()

        if not from_grid:
            self._r.capture()

        for x, y in self.iterTopCorner():
            rgb = self.getpixel(x, y, from_grid)
            if rgb not in hist:
                hist[rgb] = 0
            hist[rgb] += 1
            if hist[rgb] > max_val:
                max_val = hist[rgb]
                max_key = rgb
            if max_val > 5:
                break

        color = QColor(*max_key)
        self.type = dofus.findObject(color)

        if self.type == dofus.ObjType.UNKNOWN:
            # self.highlight(1)
            raise ParseFailed(f"Enable parse cell of top corner max color {color.getRgb()}!")

        return self.type

    def iterTopCorner(self):
        a = 0.4
        b = 0.5
        c = 0.7
        ox = self.x
        oy = self.y - (self.h / 4) * (b + c)
        w = a * self.w / 2
        h = b * self.h / 2
        return iterParallelogram(ox, oy, w, h)

    def highlight(self, secs, mode=CellOverlay.VizMode.Border):
        app = QApplication(sys.argv)
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode)
        sys.exit(app.exec_())

    def highlightTopCorner(self, secs):
        sys.excepthook = except_hook
        app = QApplication(sys.argv)
        top_corner_it = self.iterTopCorner()
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode=CellOverlay.VizMode.Shape, shape=top_corner_it)
        sys.exit(app.exec_())

    def click(self):
        env.click(self.x, self.y)

    def neighbors(self):
        if self.i % 2 == 0:
            vicinity = [(-1, 0), (1, -1), (1, 0), (-1, -1)]
        else:
            vicinity = [(-1, 1), (-1, 0), (1, 0), (1, 1)]
        for di, dj in vicinity:
            if self.grid.inside(self.i + di, self.j + dj):
                yield self.grid[self.i + di][self.j + dj]

    def inLDV(self, tgt, po):
        return self.grid.inLDV(self, tgt, po)

    def occupied(self):
        return self.type != ObjType.FREE and self.type != ObjType.REACHABLE

    def occupiedWithBot(self):
        return self.type == dofus.ObjType.BOT

    def reachable(self):
        return self.type == dofus.ObjType.REACHABLE


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
