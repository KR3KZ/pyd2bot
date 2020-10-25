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


class GridOverlay(JFrame):
    opened = set()

    def __init__(self, grid):
        super(GridOverlay, self).__init__()
        self.target_color = Color(1, 0, 0, 0.7)
        self.setAlwaysOnTop(True)
        self.setUndecorated(True)
        self.setBackground(Color(0, 0, 0, 0.0))
        self.grid = grid
        self.opened.add(self)
        self.setVisible(False)
        self.getRootPane().putClientProperty("Window.shadow", False)
        self.r = self.grid.region
        
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

    def paint(self, g):
        super(GridOverlay, self).paint(g)
        g.setStroke(BasicStroke(2))
        for row in grid:
            for cell in row:
                edge1 = Location(cell.x - self.r.x, cell.y - self.r.y + cell.h / 2)
                edge2 = Location(cell.x - self.r.x, cell.y - self.r.y - cell.h / 2)
                edge3 = Location(cell.x - self.r.x + cell.w / 2, cell.y - self.r.y)
                edge4 = Location(cell.x - self.r.x - cell.w / 2, cell.y - self.r.y)
                g.setColor(cell.type)
                g.drawLine(edge1.x, edge1.y, edge3.x, edge3.y)
                g.drawLine(edge1.x, edge1.y, edge4.x, edge4.y)
                g.drawLine(edge2.x, edge2.y, edge3.x, edge3.y)
                g.drawLine(edge2.x, edge2.y, edge4.x, edge4.y)

    def close(self):
        self.setVisible(False)
        self.opened.remove(self)
        self.dispose()

    def showWindow(self, secs):
        self.setLocation(self.grid.region.x, self.grid.region.y)
        self.setSize(self.grid.region.w, self.grid.region.h)
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class Cell(Location):

    BOT_COLOR = [Color(-65536)]
    MOB_COLOR = [Color(-16776961)]
    FREE_COLOR = [Color(-7436706), Color(-6910361)]
    OBSTACLE_COLOR = [Color(-16777216), Color(-10988742)]
    REACHABLE_COLOR = [Color(-10846914), Color(-11175624)]

    REACHABLE = Color.GREEN
    OBSTACLE = Color.RED
    MOB = Color.BLUE
    BOT = Color.MAGENTA
    FREE = Color.ORANGE

    def __init__(self, grid, x, y):
        super(Cell, self).__init__(x, y)
        self.grid = grid
        self.h = grid.cell_h
        self.w = grid.cell_w
        self._exteriorEllipse = (0.55, 0.6)
        self._interiorEllipse = (0.47, 0.45)
        self.ellipse = None
        self.type = None

    def getEllipse(self):
        if not self.ellipse:
            self.ellipse = set()
            for dy in range(-int(self.h / 2), int(self.h / 2) + 1):
                for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
                    loc = Location(dx, dy)
                    if self.insideEllipse(self._exteriorEllipse[0], self._exteriorEllipse[1], loc) and not \
                            self.insideEllipse(self._interiorEllipse[0], self._interiorEllipse[1], loc):
                        self.ellipse.add(Location(self.x + dx, self.y + dy))
        return self.ellipse

    def highlight(self, *args):
        Region(int(self.x - self.w / 2), int(self.y - self.h / 2), int(self.w), int(self.h)).highlight(*args)

    def getRGB(self, loc):
        return self.grid.getRGB(loc.x, loc.y)

    def getBorder(self):
        res = []
        for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
            dy1 = (self.h / 2) * (self.w / 2 - dx)
            dy2 = (self.h / 2) * (self.w / 2 + dx)
            res.append(Location(self.x + dx, self.y + dy1))
            res.append(Location(self.x - dx, self.y + dy2))
            res.append(Location(self.x + dx, self.y - dy1))
            res.append(Location(self.x - dx, self.y - dy2))
        return res

    def getTopCorner(self):
        # TODO
        pass

    def parse(self):
        for loc in self.ellipse:
            color = Color(self.getRGB(loc))
            if color in self.OBSTACLE_COLOR:
                self.type = self.OBSTACLE
            elif color in self.FREE_COLOR:
                self.type = self.FREE
            elif color in self.REACHABLE_COLOR:
                self.type = self.FREE_REACHABLE
            elif color in self.MOB_COLOR:
                self.type = self.MOB
            elif color in self.BOT_COLOR:
                self.type = self.BOT
            if self.type is not None:
                break
            # log.info(Color(rgb))
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

    def parse(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell_type = self[i][j].parse()
                if cell_type is None:
                    self[i][j].highlight(2)
                    raise Exception("Enable to parse cell({}, {})!".format(i, j))

    def update(self):
        self.bi = Robot().createScreenCapture(self.region.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.region.x, y - self.region.y)

    def highlight(self, secs):
        overlay = GridOverlay(self)
        overlay.showWindow(15)


if __name__ == "__main__":
    grid = Grid(COMBAT_R, NBR_V_CELL, NBR_H_CELL)
    grid.parse()
    grid.highlight(10)
