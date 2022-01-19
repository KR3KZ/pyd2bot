import sys
from time import perf_counter
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from core import dofus, env, Region
from core.utils import iterParallelogram
from gui.Overlay import CellOverlay


class Cell:

    def __init__(self, pgrid, x, y, i, j, ctype=None):
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.w = pgrid.cell_w
        self.h = pgrid.cell_h
        self.grid = pgrid
        self.extEllipse = (0.55, 0.6)
        self.type = ctype
        self.color = None
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
        max_val = 0.

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
        self.color = color
        self.type = dofus.findObject(color)

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
        # sys.excepthook = except_hook
        app = QApplication(sys.argv)
        top_corner_it = self.iterTopCorner()
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode=CellOverlay.VizMode.Shape, shape=top_corner_it)
        sys.exit(app.exec_())

    def click(self):
        self._r.click()

    def hover(self):
        self._r.hover()

    def nearBy(self, w, h):
        return self._r.nearBy(w, h)

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
        return self.type != dofus.ObjType.FREE and self.type != dofus.ObjType.REACHABLE

    def waitAppear(self, kind, timeout=3):
        start = perf_counter()
        while perf_counter() - start < timeout:
            self.parse(from_grid=False)
            if self.type == kind:
                return True
        return False

    def waitAnimation(self, timeout=3):
        return self._r.waitAnimationEnd(timeout)

    def reachable(self):
        return self.type == dofus.ObjType.REACHABLE

    def opaque(self):
        return self.type == dofus.ObjType.OBSTACLE or \
               self.type == dofus.ObjType.MOB or \
               self.type == dofus.ObjType.INVOKE

    def indexes(self):
        return self.i, self.j
