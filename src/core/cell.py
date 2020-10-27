from math import sqrt

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor

from core.env import ObjColor, ObjType
from gui.Overlay import CellOverlay


def _iterParallelogram(o, w, h):
    for dx in range(-int(w / 2), int(w / 2) + 1):
        max_dy = int((h / w) * (w / 2 - abs(dx)))
        for dy in range(-max_dy, max_dy + 1):
            yield QPoint(o.x + dx, o.y + dy)


class Cell:

    def __init__(self, pgrid, x, y):
        self.x = x
        self.y = y
        self.grid = pgrid
        self.h = pgrid.cell_h
        self.w = pgrid.cell_w
        self.extEllipse = (0.55, 0.6)
        self.type = ObjType.UNKNOWN
        self.rx, self.ry = self.x - self.grid.r.x, self.y - self.grid.r.y

    def __iter__(self):
        return _iterParallelogram(self, self.w, self.h)

    def __contains__(self, loc):
        res = self.w * abs(loc.y) + self.h * (abs(loc.x) - self.w / 2) <= 0
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

    def getRGB(self, loc):
        return self.grid.getRGB(loc.x, loc.y)

    def parse(self):
        hist = {}
        max_key = None
        max_val = 0

        unknown = set()

        for loc in self.iterTopCorner():
            color = self.getRGB(loc)
            if color not in hist:
                hist[color] = 0
            hist[color] += 1
            if hist[color] > max_val:
                max_val = hist[color]
                max_key = color
            if max_val > 9:
                break

        max_key = QColor(max_key)

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
            if max_key not in unknown:
                log.info(max_key)
                unknown.add(max_key)
            self.type = max_key

        return self.type

    def iterTopCorner(self):
        a = 0.4
        b = 0.5
        c = 0.7
        o = QPoint(self.x, self.y - (self.h / 4) * (b + c))
        w = a * self.w / 2
        h = b * self.h / 2
        return _iterParallelogram(o, w, h)

    def highlight(self, secs, mode=CellOverlay.VizMode.Border):
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode)

    def highlightTopCorner(self, secs):
        top_corner_it = map(lambda l: (QColor.green, l), self.iterTopCorner())
        overlay = CellOverlay(self)
        overlay.highlight(secs, mode=CellOverlay.VizMode.Shape, shape=top_corner_it)
