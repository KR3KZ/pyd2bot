import sys
from itertools import product
from math import floor
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from core import dofus
from core.cell import Cell
from core.region import Region
from core.utils import sample
from gui.Overlay import GridOverlay
import core.env as env


class Grid(Region):

    def __init__(self, region, nbr_vcell, nbr_hcell):
        super(Grid, self).__init__(*region.getRect())
        self.unknown = []
        self.nbr_vcell = nbr_vcell
        self.nbr_hcell = nbr_hcell
        self.cell_w = self.width() / nbr_hcell
        self.cell_h = self.height() / nbr_vcell
        self._matrix = []
        self.bot = None
        self.mobs = set()
        self.reachable = set()
        self.free = set()
        self.non_obstacle = set()
        self.invoke = set()
        nrow = 0
        ncol = 0
        for i in range(1, int(2 * self.nbr_vcell)):
            row = []
            ncol = 0
            for j in range(1, int(2 * self.nbr_hcell)):
                if (i + j) % 2 == 0:
                    cell_x = self.x() + int(j * self.cell_w / 2)
                    cell_y = self.y() + int(i * self.cell_h / 2)
                    row.append(Cell(self, cell_x, cell_y, nrow, ncol))
                    ncol += 1
            self._matrix.append(row)
            nrow += 1
        self.rows = len(self._matrix)
        self.cols = len(self._matrix[0])

    def __getitem__(self, idx):
        return self._matrix[idx]

    def __iter__(self):
        for row in self._matrix:
            for cell in row:
                yield cell

    def inLDV(self, cell, mob, po):
        if self.dist(cell, mob) > po:
            return False
        elif self.dist(cell, mob) == 1:
            return True
        for i, j in self.getLdvCells(cell, mob):
            if self[i][j].opaque():
                return False
        return True

    def getLdvCells(self, c1, c2):
        w = self.cell_w
        yielded = {(c1.i, c1.j), (c2.i, c2.j)}
        if c1.x > c2.x:
            c1, c2 = c2, c1
        if abs(c2.rx - c1.rx) < w / 4:
            start = min(c1.i, c2.i) + 1
            end = max(c1.i, c2.i)
            for i in range(start, end):
                if i % 2 == c1.i % 2:
                    yield i, c1.j
        else:
            alpha = (c2.y - c1.y) / (c2.x - c1.x)
            for x in sample(c1.rx, c2.rx, 50000):
                if abs(2 * x / w - round(2 * x / w)) <= 1e-20:
                    continue
                y = alpha * (x - c1.rx) + c1.ry
                res = self.getByCoords(x, y)
                if res not in yielded:
                    yielded.add(res)
                    yield res

    def getByCoords(self, x, y, relative=True):
        if not relative:
            x = x - self.x()
            y = y - self.y()
        ny = 2 * y / self.cell_h
        nx = 2 * x / self.cell_w
        iRange = [floor(ny) + eps for eps in range(2)]
        jRange = [floor(nx) + eps for eps in range(2)]
        for i, j in product(iRange, jRange):
            if (j + i) % 2 == 0 and abs(ny - i) + abs(nx - j) <= 1:
                return i - 1, floor((j - 1) / 2)

    def parse(self, do_parse=True):
        self.bot = None
        self.mobs = set()
        self.reachable = set()
        self.free = set()
        self.capture()
        self.unknown = []
        for cell in self:

            if do_parse:
                ctype = cell.parse()
            else:
                ctype = cell.type

            if ctype == dofus.ObjType.BOT:
                self.bot = cell
            elif ctype == dofus.ObjType.MOB:
                self.mobs.add(cell)
            elif ctype == dofus.ObjType.FREE:
                self.free.add(cell)
            elif ctype == dofus.ObjType.REACHABLE:
                self.reachable.add(cell)
            elif ctype == dofus.ObjType.INVOKE:
                self.invoke.add(cell)
            elif ctype == dofus.ObjType.UNKNOWN:
                self.unknown.append(cell)

        if len(self.unknown) == 1:
            if not self.mobs:
                self.unknown[0].type = dofus.ObjType.MOB
                self.mobs.add(self.unknown[0])
            elif not self.bot:
                self.unknown[0].type = dofus.ObjType.BOT
                self.bot = self.unknown[0]
            else:
                # assume its an obstacle (to test)
                self.unknown[0].type = dofus.ObjType.OBSTACLE

        elif len(self.unknown) > 1:
            return False

        if not self.bot or not self.mobs:
            return False

        return True

    def dist(self, cell1, cell2):
        i = 2 * abs(cell1.x - cell2.x) / self.cell_w
        j = 2 * abs(cell1.y - cell2.y) / self.cell_h
        return max(round(i), round(j))

    def highlight(self, secs):
        app = QApplication(sys.argv)
        self.overlay = GridOverlay(self)
        self.overlay.highlight(secs)
        sys.exit(app.exec_())

    def to_dict(self):
        return {
            "map": [[{"i": i, "j": j, "type": QColor(self[i][j].type).getRgb()} for i in range(self.rows)] for j in
                    range(self.cols)]}

    def fromJson(self, path_to_file):
        import json
        with open(path_to_file, 'r') as f:
            data = json.load(f)
        for row in data["map"]:
            for cell in row:
                self[cell["i"]][cell["j"]].type = QColor(*cell["type"])
        self.parse(do_parse=False)

    def inside(self, i, j):
        return 0 <= i <= self.rows - 1 and 0 <= j <= self.cols - 1


if __name__ == "__main__":
    env.focusDofusWindow()
    grid = Grid(dofus.COMBAT_R, dofus.VCELLS, dofus.HCELLS)
    grid.parse()
    grid.highlight(5)
    grid.overlay.highlightEnded.connect(env.focusIDEWindow)
