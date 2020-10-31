import sys
from itertools import product
from math import floor
from time import sleep
from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from core.cell import Cell
from core.log import Log
from gui.Overlay import GridOverlay
import core.env as env
import pyautogui

log = Log()


class Grid(QRect):

    def __init__(self, region, nbr_vcell, nbr_hcell):
        super(Grid, self).__init__(*region.getRect())
        self.nbr_vcell = nbr_vcell
        self.nbr_hcell = nbr_hcell
        self.cell_w = self.width() / nbr_hcell
        self.cell_h = self.height() / nbr_vcell
        self.bi = pyautogui.screenshot(region=self.getRect())
        self._matrix = []
        self.bot = None
        self.mobs = set()
        self.reachable = set()
        self.free = set()
        self.non_obstacle = set()
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

    @staticmethod
    def getLdvCells(c1, c2):
        w = c1.w
        h = c1.h
        yielded = set()
        if abs(c2.rx - c1.rx) < w / 4:
            for i in range(c1.i, c2.i + 1):
                if i % 2 == 0:
                    yield i, c1.j
        else:
            if c1.x > c2.x:
                c1, c2 = c2, c1
            alpha = (c2.y - c1.y) / (c2.x - c1.x)
            for x in range(c1.rx, c2.rx + 1):
                nx = 2 * x / w
                if abs(nx - round(nx)) <= 2 / w:
                    continue
                y = alpha * (x - c1.rx) + c1.ry
                ny = 2 * y / h
                iRange = [floor(ny) + eps for eps in range(2)]
                jRange = [floor(nx) + eps for eps in range(2)]
                for i, j in product(iRange, jRange):
                    if (j + i) % 2 == 0 and abs(ny - i) + abs(nx - j) <= 1:
                        result = (i - 1, floor((j - 1) / 2))
                        if result not in yielded:
                            yielded.add(result)
                            yield result

    def parse(self):
        self.bot = None
        self.mobs = set()
        self.reachable = set()
        self.free = set()
        if not self.non_obstacle:
            to_iter = self
        else:
            to_iter = self.non_obstacle
        for cell in to_iter:
            ctype = cell.parse()
            if ctype == env.ObjType.BOT:
                self.bot = cell
            elif ctype == env.ObjType.MOB:
                self.mobs.add(cell)
            elif ctype == env.ObjType.FREE:
                self.free.add(cell)
            elif ctype == env.ObjType.REACHABLE:
                self.reachable.add(cell)
        self.non_obstacle = self.mobs | self.free | self.reachable
        self.non_obstacle.add(self.bot)

    def update(self):
        self.bi = pyautogui.screenshot(region=self.getRect())

    def getpixel(self, p):
        target = (p.x() - self.x(), p.y() - self.y())
        rgb = self.bi.getpixel(target)
        return QColor(*rgb)

    def dist(self, cell1, cell2):
        i = abs(cell1.x() - cell2.x()) / self.cell_w
        j = abs(cell1.y() - cell2.y()) / self.cell_h
        return max(int(i), int(j))

    def distx(self, cell1, cell2):
        j = abs(cell1.y() - cell2.y()) / self.cell_h
        return int(j)

    def highlight(self, secs):
        app = QApplication(sys.argv)
        self.overlay = GridOverlay(self)
        self.overlay.highlight(secs)
        sys.exit(app.exec_())

    def to_dict(self):
        return {
            "map": [[{"i": i, "j": j, "type": self[i][j].type.getRgb()} for i in range(self.rows)] for j in
                    range(self.cols)]}

    def fromJson(self, path_to_file):
        import json
        with open(path_to_file, 'rect') as f:
            data = json.load(f)
        for row in data["map"]:
            for cell in row:
                self[cell["i"]][cell["j"]].type = QColor(*cell["type"])


if __name__ == "__main__":
    sleep(2)
    grid = Grid(env.COMBAT_R, env.VCELLS, env.HCELLS)
    grid.parse()
    grid[22][5].highlightTopCorner(2)
