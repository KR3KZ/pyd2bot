from java.awt import Color, Rectangle, AlphaComposite, RenderingHints, BasicStroke, Toolkit, Robot
from javax.swing import JFrame
from java.awt.geom import Path2D
import traceback
import logging
from math import sqrt
from sikuli.Sikuli import *


class DofusGUI:
    COMBAT_R = Region(335, 29, 1253, 885)
    HCELLS = 14.5
    VCELLS = 20.5


class Log:
    def __init__(self):
        format = "<%(asctime)-15s %(levelname)s line %(lineno)d %(threadName)s> %(funcName)s: - %(message)s"
        logging.basicConfig(level=logging.INFO, format=format)
        self.log = logging.getLogger("bot logger")

    def info(self, *args):
        res = ', '.join(map(str, args))
        self.log.info(res)


log = Log()


class Overlay(JFrame):
    opened = set()

    def __init__(self):
        super(Overlay, self).__init__()
        self.target_color = Color(1, 0, 0, 0.7)
        self.setAlwaysOnTop(True)
        self.setUndecorated(True)
        self.setBackground(Color(0, 0, 0, 0.0))
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

    def paint(self, g):
        stroke = BasicStroke(3)
        g.setColor(self.target_color)
        g.setStroke(stroke)
        w = stroke.getLineWidth()
        g.drawRect(int(w / 2), int(w / 2), int(self.getWidth() - w), int(self.getHeight() - w))

    def close(self):
        self.setVisible(False)
        self.opened.remove(self)
        self.dispose()

    def highlight(self, r, secs):
        self.setLocation(r.x, r.y)
        self.setSize(r.w, r.h)
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class ObjColor:
    BOT = [Color(-65536)]
    MOB = [Color(-16776961)]
    FREE = [Color(-7436706), Color(-6910361)]
    OBSTACLE = [Color(-16777216), Color(-10988742)]
    REACHABLE = [Color(-10846914), Color(-11175624)]


class ObjType:
    REACHABLE = Color.GREEN
    OBSTACLE = Color.RED
    MOB = Color.BLUE
    BOT = Color.MAGENTA
    FREE = Color.ORANGE
    UNKNOWN = Color.WHITE


class CellOverlay(Overlay):
    
    class VizMode:
        BORDER = 1
        ELLIPSE = 2
        FILL = 3

    def __init__(self, cell, mode=VizMode.BORDER):
        self.cell = cell
        self.mode = mode
        self.setLocation(int(self.cell.x - self.cell.w / 2), int(self.cell.y - self.cell.h / 2))
        self.cell.setSize(self.cell.w, self.h)

    def drawEllipse(self, g):
        w = self.cell.extEllipse[0] * self.cell.w / 2
        h = self.cell.extEllipse[1] * self.cell.h / 2
        g.setColor(self.cell.type)
        g.setStroke(BasicStroke(2))
        g.drawOval(0, 0, w, h)

    def drawBorder(self, g):
        g.setStroke(BasicStroke(2))
        parallelogram = Path2D.Double
        g.setColor(self.cell.type)
        parallelogram.moveTo(self.cell.rx + self.cell.w / 2, self.cell.y + self.cell.h)
        parallelogram.lineTo(self.cell.rx + self.cell.w, self.cell.y + self.cell.h / 2)
        parallelogram.lineTo(self.cell.rx + self.cell.w / 2, self.cell.y)
        parallelogram.lineTo(self.cell.rx, self.cell.y + self.cell.h / 2)
        parallelogram.closePath()
        g.fill(parallelogram)

    def fill(self, g):
        pass

    def paint(self, g):
        super(Overlay, self).paint(g)
        if self.mode == Cell.VizMode.BORDER:
            self.drawBorder(g)
        elif self.mode == Cell.VizMode.ELLIPSE:
            self.drawEllipse(g)
        elif self.mode == Cell.VizMode.FILL:
            self.fill(g)

    def highlight(self, secs):
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class GridOverlay(Overlay):

    def __init__(self, grid):
        super(Overlay, self).__init__()
        self.grid = grid
        self.r = self.grid.r
        self.setLocation(self.r.x, self.r.y)
        self.setSize(self.r.w, self.r.h)

    def paint(self, g):
        super(Overlay, self).paint(g)
        g.setStroke(BasicStroke(2))
        for row in self.grid:
            for cell in row:
                g.setStroke(BasicStroke(2))
                parallelogram = Path2D.Double()
                g.setColor(cell.type)
                parallelogram.moveTo(cell.x - self.r.x, cell.y - self.r.y + cell.h / 2)
                parallelogram.lineTo(cell.x - self.r.x + cell.w / 2, cell.y - self.r.y)
                parallelogram.lineTo(cell.x - self.r.x, cell.y - self.r.y - cell.h / 2)
                parallelogram.lineTo(cell.x - self.r.x - cell.w / 2, cell.y - self.r.y)
                parallelogram.closePath()
                g.fill(parallelogram)

    def highlight(self, secs):
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class Cell(Location):

    def __init__(self, pgrid, x, y):
        super(Location, self).__init__(x, y)
        self.grid = pgrid
        self.h = pgrid.cell_h
        self.w = pgrid.cell_w
        self.extEllipse = (0.55, 0.6)
        self.type = ObjType.UNKNOWN
        self.rx, self.ry = self.x - self.grid.r.x, self.y - self.grid.r.y

    def __iter__(self):
        for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
            max_dy = int((self.h / self.w) * abs(dx - self.w / 2))
            for dy in range(-max_dy, max_dy + 1):
                yield Location(self.x + dx, self.y + dy)

    def __contains__(self, loc):
        res = self.w * abs(loc.y) + self.h * (abs(loc.x) - self.w / 2) <= 0
        return res

    def iterEllipse(self, thickness=2):
        a = self.extEllipse[0] * self.w / 2
        b = self.extEllipse[1] * self.h / 2
        for dx in range(int(a) + 1):
            dy = int(b * sqrt(1 - (dx / a) ** 2))
            for eps in range(thickness):
                yield Location(self.x + dx, self.y + dy - eps)
                yield Location(self.x + dx, self.y - dy - eps)
                yield Location(self.x - dx, self.y + dy - eps)
                yield Location(self.x - dx, self.y - dy - eps)

    def getRGB(self, loc):
        return self.grid.getRGB(loc.x, loc.y)

    def parseFromTopCorner(self):
        # TODO
        pass

    def parseFromEllipse(self):
        self.type = ObjType.UNKNOWN
        for loc in self.iterEllipse():
            color = Color(self.getRGB(loc))
            if color in ObjColor.OBSTACLE:
                self.type = ObjType.OBSTACLE
            elif color in ObjColor.FREE:
                self.type = ObjType.FREE
            elif color in ObjColor.REACHABLE:
                self.type = ObjType.REACHABLE
            elif color in ObjColor.MOB:
                self.type = ObjType.MOB
            elif color in ObjColor.BOT:
                self.type = ObjType.BOT
            if self.type != ObjType.UNKNOWN:
                break
        return self.type

    def highlight(self, secs, mode):
        overlay = CellOverlay(self, mode)
        overlay.highlight(secs)


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
        for i in range(self.rows):
            for j in range(self.cols):
                cell_type = self[i][j].parseFromEllipse()
                if cell_type is None:
                    self[i][j].highlight(2)
                    raise Exception("Enable to parse cell({}, {})!".format(i, j))

    def update(self):
        self.bi = Robot().createScreenCapture(self.r.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.r.x, y - self.r.y)

    def highlight(self, secs):
        overlay = GridOverlay(self)
        overlay.highlight(secs)


if __name__ == "__main__":
    grid = Grid(DofusGUI.COMBAT_R, DofusGUI.VCELLS, DofusGUI.HCELLS)
    grid.parse()
    grid.highlight(10)
