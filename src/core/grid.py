import sys
from time import sleep

from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

from core.cell import Cell
from core.log import Log
from gui.Overlay import GridOverlay
import core.env as env
import cv2
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
        for i in range(1, int(2 * self.nbr_vcell)):
            row = []
            for j in range(1, int(2 * self.nbr_hcell)):
                if (i + j) % 2 == 0:
                    cell_x = self.x() + int(j * self.cell_w / 2)
                    cell_y = self.y() + int(i * self.cell_h / 2)
                    row.append(Cell(self, cell_x, cell_y))
            self._matrix.append(row)
        self.rows = len(self._matrix)
        self.cols = len(self._matrix[0])

    def __getitem__(self, idx):
        return self._matrix[idx]

    def parse(self):
        for i in range(1, self.rows):
            for j in range(self.cols):
                self[i][j].parse()

    def update(self):
        self.bi = pyautogui.screenshot(region=self.getRect())
        self.parse()

    def getpixel(self, p):
        target = (p.x() - self.x(), p.y() - self.y())
        rgb = self.bi.getpixel(target)
        return QColor(*rgb)

    def highlight(self, secs):
        app = QApplication(sys.argv)
        overlay = GridOverlay(self)
        overlay.highlight(secs)
        sys.exit(app.exec_())

    def to_dict(self):
        return {
            "map": [[{"i": i, "j": j, "type": self[i][j].type.getRgb()} for i in range(self.rows)] for j in
                    range(self.cols)]}

    def fromJson(self, path_to_file):
        import json
        with open(path_to_file, 'r') as f:
            data = json.load(f)
        for row in data["map"]:
            for cell in row:
                self[cell["i"]][cell["j"]].type = QColor(*cell["type"])


if __name__ == "__main__":
    sleep(2)
    grid = Grid(env.Region.COMBAT_R, env.VCELLS, env.HCELLS)
    grid.parse()
    grid.highlight(2)
