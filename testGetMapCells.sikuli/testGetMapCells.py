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


class Grid(list):
    def __init__(self, region, nbr_vcell, nbr_hcell):
        list.__init__(self)
        self.nbr_vcell = nbr_vcell
        self.nbr_hcell = nbr_hcell
        self.region = region
        self.CELL_W = region.w / nbr_hcell
        self.CELL_H = region.h / nbr_vcell
        for i in range(1, int(2 * NBR_V_CELL)):
            row = []
            for j in range(1, int(2 * NBR_H_CELL)):
                if (i + j) % 2 == 0:
                    cell_x = region.x + int(j * self.CELL_W / 2)
                    cell_y = region.y + int(i * self.CELL_H / 2)
                    row.append(Location(cell_x, cell_y))
            self.append(row)
        self.rows = len(self)
        self.cols = len(self[0])


SRC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


def get_log():
    format = "<%(asctime)-15s %(threadName)s %(funcName)s> %(message)s"
    log_path = os.path.join(SRC_DIR, "bot.log")
    logging.basicConfig(level=logging.INFO, format=format)
    return logging.getLogger("bot logger")


# bot log
log = get_log()

COMBAT_R = Region(335, 29, 1253, 885)
NBR_H_CELL = 14.5
NBR_V_CELL = 20.5


def getNearBy(loc, w, h):
    return Region(loc.x - w / 2, loc.y - h / 2, w, h)


def isKnown(colorsDB, color):
    for cat, items in colorsDB.items():
        if color in items:
            return True
    return False


def teachBotColors():
    snippet = Robot().createScreenCapture(Rectangle(COMBAT_R.x, COMBAT_R.y, COMBAT_R.w, COMBAT_R.h))
    grid = Grid(COMBAT_R, NBR_V_CELL, NBR_H_CELL)
    categories = ("obstacle", "mob", "bot", "free square", "free reachable square")
    colorsDB = loadColorDB()
    if not colorsDB:
        colorsDB = {it: [] for it in categories}
    nrows = len(grid)
    ncols = len(grid[0])
    for i in range(nrows):
        for j in range(ncols):
            cell_color = snippet.getRGB(grid[i][j].x - COMBAT_R.x - int(grid.CELL_W / 4), grid[i][j].y - COMBAT_R.y)
            if cell_color != Color(0, 0, 0) and not isKnown(colorsDB, cell_color):
                getNearBy(grid[i][j], int(grid.CELL_W), int(grid.CELL_H)).highlight('green')
                selected = select("what is that daddy ?", options=categories)
                if selected not in colorsDB:
                    colorsDB[selected] = []
                colorsDB[selected].append(cell_color)
    saveColorDB(colorsDB)


def loadColorDB():
    colordb_path = os.path.join(SRC_DIR, "colorsdb.txt")
    with open(colordb_path, 'r') as f:
        data = json.load(f)
    return data


def saveColorDB(data):
    colordb_path = os.path.join(SRC_DIR, "colorsdb.txt")
    with open(colordb_path, 'w') as outfile:
        json.dump(data, outfile)


print(Color(-16776961))
