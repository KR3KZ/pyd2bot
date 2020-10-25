from java.awt import Color, Rectangle, AlphaComposite, RenderingHints, BasicStroke, Toolkit, Robot
from java.awt.image import BufferedImage
import java.io.File
import java.io.IOException
from javax.imageio import ImageIO
import time
import logging
import json
from javax.swing import JFrame, ImageIcon
import traceback
import logging

SRC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
COMBAT_R = Region(335, 29, 1253, 885)
NBR_H_CELL = 14.5
NBR_V_CELL = 20.5


class Log:
    def __init__(self):
        format = "<%(asctime)-15s %(levelname)s line %(lineno)d %(threadName)s> %(funcName)s: - %(message)s"
        logging.basicConfig(level=logging.INFO, format=format)
        self.log = logging.getLogger("bot logger")

    def info(self, *args):
        res = ', '.join(map(str, args))
        self.log.info(res)


log = Log()


class ScreenHighlighter(JFrame):
    opened = set()

    def __init__(self):
        super(ScreenHighlighter, self).__init__()
        self.target_color = Color(1, 0, 0, 0.7)
        self.setAlwaysOnTop(True)
        self.setUndecorated(True)
        self.setBackground(Color(0, 0, 0, 0.0))
        self.roi = set()
        self.opened.add(self)
        self.setVisible(False)
        self.getRootPane().putClientProperty("Window.shadow", False)

    def closeAfter(self, secs):
        try:
            sleep(secs)
        except InterruptedError as e:
            self.close()
            traceback.print_stack()
        self.close()

    def drawBorder(self, g):
        stroke = BasicStroke(3)
        g.setColor(self.target_color)
        g.setStroke(stroke)
        w = stroke.getLineWidth()
        g.drawRect(int(w / 2), int(w / 2), int(self.getWidth() - w), int(self.getHeight() - w))

    def drawRoi(self, g):
        for points, color in self.roi:
            g.setColor(color)
            for loc in points:
                g.drawLine(loc.x, loc.y, loc.x, loc.y)

    def paint(self, g):
        super(ScreenHighlighter, self).paint(g)
        if not self.roi:
            self.drawBorder(g)
        else:
            self.drawRoi(g)

    def close(self):
        self.setVisible(False)
        self.opened.remove(self)
        self.dispose()

    def highlight(self, r, secs=None, roi=None, color=None):
        self.setLocation(r.x, r.y)
        self.setSize(r.w, r.h)
        if roi:
            self.roi = roi
        if color:
            self.target_color = color
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class CellType:
    FREE_REACHABLE = 5
    OBSTACLE = 0
    MOB = 1
    BOT = 2
    FREE = 3
    REACHABLE = 4


class ObjColor:
    BOT = [-65536]
    MOB = [-16776961]
    FREE = [-7436706, -6910361]
    OBSTACLE = [-16777216, -10988742]
    FREE_REACHABLE = [-10846914, -11175624]


class Cell(Location):

    def __init__(self, grid, x, y):
        super(Cell, self).__init__(x, y)
        self.grid = grid
        self.h = grid.cell_h
        self.w = grid.cell_w
        self.ellipse = self.getEllipse()
        self.type = None

    def getEllipse(self):
        res = set()
        for dy in range(-int(self.h / 2), int(self.h / 2) + 1):
            for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
                loc = Location(dx, dy)
                if self.insideEllipse(self._exteriorEllipse[0], self._exteriorEllipse[1], loc) and not \
                        self.insideEllipse(self._interiorEllipse[0], self._interiorEllipse[1], loc):
                    res.add(Location(self.x + dx, self.y + dy))
        return res

    def highlight(self, *args):
        Region(int(self.x - self.w / 2), int(self.y - self.h / 2), int(self.w), int(self.h)).highlight(*args)

    def getRGB(self, loc):
        self.grid.bi.getRGB(loc.x, loc.y)

    def parse(self):
        for loc in self.ellipse:
            if self.getRGB(loc) in ObjColor.OBSTACLE:
                self.type = CellType.OBSTACLE
            elif self.getRGB(loc) in ObjColor.FREE:
                self.type = CellType.FREE
            elif self.getRGB(loc) in ObjColor.FREE_REACHABLE:
                self.type = CellType.FREE_REACHABLE
            elif self.getRGB(loc) in ObjColor.MOB:
                self.type = CellType.MOB
            elif self.getRGB(loc) in ObjColor.BOT:
                self.type = CellType.BOT
            if self.type is not None:
                break
        return self.type

    def insideEllipse(self, a, b, loc):
        w = a * self.w / 2
        h = b * self.h / 2
        return (loc.x / w) ** 2 + (loc.y / h) ** 2 <= 1

    def __iter__(self):
        for dy in range(-int(self.h / 2), int(self.h / 2) + 1):
            for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
                if Location(dx, dy) in self:
                    yield Location(self.x + dx, self.y + dy)

    def __contains__(self, loc):
        res = self.w * abs(loc.y) + self.h * (abs(loc.x) - self.w / 2) <= 0
        return res


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
        self._exteriorEllipse = (0.55, 0.6)
        self._interiorEllipse = (0.47, 0.45)

    def parse(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell_type = self[i][j].parse()
                if not cell_type:
                    raise Exception("Enable to parse cell({}, {})!".format(i, j))

    def update(self):
        self.bi = Robot().createScreenCapture(self.region.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.region.x, y - self.region.y)


if __name__ == "__main__":
    overlay = ScreenHighlighter()
    grid = Grid(COMBAT_R, NBR_V_CELL, NBR_H_CELL)
    grid.parse()
    overlay = ScreenHighlighter()
    for i in grid.rows:
        for j in grid.cols:
            color = None
            if grid[i][j].type == CellType.OBSTACLE:
                color = Color.RED
            elif grid[i][j].type == CellType.FREE:
                color = Color.ORANGE
            elif grid[i][j].type == CellType.FREE_REACHABLE:
                color = Color.GREEN
            elif grid[i][j].type == CellType.MOB:
                color = Color.BLUE
            elif grid[i][j].type == CellType.BOT:
                color = Color.MAGENTA
            overlay.roi += (grid[i][j], color)
    overlay.highlight(COMBAT_R, 15)
