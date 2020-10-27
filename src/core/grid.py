from PyQt5.QtCore import QRect, QPoint
from core.log import Log
from gui.Overlay import GridOverlay
import core.env as env
import cv2
import pyautogui

log = Log()





class Grid(list):

    def __init__(self, region, nbr_vcell, nbr_hcell):
        list.__init__(self)
        self.nbr_vcell = nbr_vcell
        self.nbr_hcell = nbr_hcell
        self.r = region
        self.cell_w = region.w / nbr_hcell
        self.cell_h = region.h / nbr_vcell
        self.bi = Robot().createScreenCapture(region.getRect())
        for i in range(1, int(2 * self.nbr_vcell)):
            row = []
            for j in range(1, int(2 * self.nbr_hcell)):
                if (i + j) % 2 == 0:
                    cell_x = region.x + int(j * self.cell_w / 2)
                    cell_y = region.y + int(i * self.cell_h / 2)
                    row.append(Cell(self, cell_x, cell_y))
            self.append(row)
        self.rows = len(self)
        self.cols = len(self[0])

    def parse(self):
        for i in range(1, self.rows):
            for j in range(self.cols):
                self[i][j].parse()

    def update(self):
        self.bi = Robot().createScreenCapture(self.r.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.r.x, y - self.r.y)

    def highlight(self, secs):
        overlay = GridOverlay(self)
        overlay.highlight(secs)


if __name__ == "__main__":
    grid = Grid(env.COMBAT_R, env.VCELLS, env.HCELLS)
    grid.parse()
    grid.highlight(2)
