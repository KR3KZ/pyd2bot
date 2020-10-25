from java.awt import Robot
from java.awt import Color
from java.awt import Rectangle
import java.awt.Color as Color
import java.awt.Toolkit
import java.awt.image.BufferedImage
import java.io.File
import java.io.IOException
import javax.imageio.ImageIO as ImageIO
import time
import logging
import json

SRC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
COMBAT_R = Region(335, 29, 1253, 885)
NBR_H_CELL = 14.5
NBR_V_CELL = 20.5


class CellType:
    OBSTACLE = 0
    MOB = 1
    BOT = 2
    FREE = 3
    REACHABLE = 4


class Cell(Location):

    def __init__(self, grid, x, y):
        super().__init__(self, x, y)
        self.grid = grid
        self.h = grid.cell_h
        self.w = grid.cell_w
        self.ellipse = self.getEllipse()

    def highlight(self, *args):
        Region(self.x - self.w / 2, self.y - self.h / 2, self.w, self.h).highlight(*args)

    def getRgb(self, dx, dy):
        self.grid.bi.getRGB(self.x + dx, self.y + dy)

    def parse(self):
        pass

    def getEllipse(self):
        res = []
        for i in range(-int(self.h / 2), int(self.h / 2) + 1):
            for j in range(-int(self.w / 2), int(self.w / 2) + 1):
                if i >= self.h / 4 and j >= self.w / 4 and Location(i, j) in self:
                    res.appen((i, j))
        return res

    def __contains__(self, loc):
        return self.w * abs(loc.y) + self.h * (abs(loc.x) - self.w / 2)


class Grid(list):
    def __init__(self, region, nbr_vcell, nbr_hcell):
        list.__init__(self)
        self.nbr_vcell = nbr_vcell
        self.nbr_hcell = nbr_hcell
        self.region = region
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
        pass

    def update(self):
        self.bi = Robot().createScreenCapture(self.region.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.region.x, y - self.region.y)
