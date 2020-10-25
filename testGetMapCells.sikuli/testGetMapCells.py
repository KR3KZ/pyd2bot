from java.awt import Color, Rectangle, AlphaComposite, RenderingHints, BasicStroke, Toolkit, Robot
import time
import logging
from javax.swing import JFrame, ImageIcon
from java.awt.geom import Path2D
import traceback
import logging
from math import sqrt
from sikuli.Sikuli import *

SRC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


class DofusGUI:
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

    def showWindow(self, r, secs):
        self.setLocation(r.r.x, r.r.y)
        self.setSize(r.r.w, r.r.h)
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class ObjColor:
    BOT_COLOR = [Color(-65536)]
    MOB_COLOR = [Color(-16776961)]
    FREE_COLOR = [Color(-7436706), Color(-6910361)]
    OBSTACLE_COLOR = [Color(-16777216), Color(-10988742)]
    REACHABLE_COLOR = [Color(-10846914), Color(-11175624)]


class ObjType:
    REACHABLE = Color.GREEN
    OBSTACLE = Color.RED
    MOB = Color.BLUE
    BOT = Color.MAGENTA
    FREE = Color.ORANGE
    UNKNOWN = Color.WHITE


class Cell(Location, Overlay):
    class VizMode:
        BORDER = 1
        ELLIPSE = 2
        FILL = 3

    def __init__(self, pgrid, x, y, mode=VizMode.BORDER):
        super(Location, self).__init__(x, y)
        self.grid = pgrid
        self.h = pgrid.cell_h
        self.w = pgrid.cell_w
        self.extEll = (0.55, 0.6)
        self.ellipse = set()
        self.type = ObjType.UNKNOWN
        self.mode = mode
        self.rx, self.ry = self.x - self.grid.x, self.y - self.grid.y

    def __iter__(self):
        for dx in range(-int(self.w / 2), int(self.w / 2) + 1):
            max_dy = int((self.h / self.w) * abs(dx - self.w / 2))
            for dy in range(-max_dy, max_dy + 1):
                yield Location(self.x + dx, self.y + dy)

    def __contains__(self, loc):
        res = self.w * abs(loc.y) + self.h * (abs(loc.x) - self.w / 2) <= 0
        return res

    def getEllipse(self, thickness=2):
        w = self.extEll[0] * self.w / 2
        h = self.extEll[1] * self.h / 2
        if not self.ellipse:
            self.ellipse = set()
            for dx in range(int(w) + 1):
                dy = int((h / 2) * sqrt(1 - (2 * dx / w) ** 2))
                for eps in range(thickness):
                    self.ellipse.update({Location(self.x + dx, self.y + dy - eps),
                                         Location(self.x + dx, self.y - dy - eps),
                                         Location(self.x - dx, self.y + dy - eps),
                                         Location(self.x - dx, self.y - dy - eps)})
        return self.ellipse

    def getRGB(self, loc):
        return self.grid.getRGB(loc.x, loc.y)

    def getTopCorner(self):
        # TODO
        pass

    def parse(self):
        for loc in self.ellipse:
            color = Color(self.getRGB(loc))
            if color in ObjColor.OBSTACLE_COLOR:
                self.type = self.OBSTACLE
            elif color in ObjColor.FREE_COLOR:
                self.type = self.FREE
            elif color in ObjColor.REACHABLE_COLOR:
                self.type = self.REACHABLE
            elif color in ObjColor.MOB_COLOR:
                self.type = self.MOB
            elif color in ObjColor.BOT_COLOR:
                self.type = self.BOT
            if self.type is not None:
                break
            # log.info(Color(rgb))
        return self.type

    def drawEllipse(self, g):
        w = self.extEll[0] * self.w / 2
        h = self.extEll[1] * self.h / 2
        g.setColor(self.type)
        g.setStroke(BasicStroke(2))
        g.drawOval(0, 0, w, h)

    def drawBorder(self, g):
        g.setStroke(BasicStroke(2))
        parallelogram = Path2D.Double
        g.setColor(self.type)
        parallelogram.moveTo(self.rx + self.w / 2, self.y + self.h)
        parallelogram.lineTo(self.rx + self.w, self.y + self.h / 2)
        parallelogram.lineTo(self.rx + self.w / 2, self.y)
        parallelogram.lineTo(self.rx, self.y + self.h / 2)
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
        self.setLocation(int(self.x - self.w / 2), int(self.y - self.h / 2))
        self.setSize(self.w, self.h)
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


class Grid(list, Overlay):

    def __init__(self, r, vcells, hcells):
        list.__init__(self)
        self.vcells = vcells
        self.hcells = hcells
        self.r = r
        self.cell_w = r.w / hcells
        self.cell_h = r.h / vcells
        self.bi = Robot().createScreenCapture(r.getRect())
        self.x = r.x
        self.y = r.y
        self.h = r.h
        self.w = r.w

        for i in range(1, int(2 * self.vcells)):
            row = []
            for j in range(1, int(2 * self.hcells)):
                if (i + j) % 2 == 0:
                    cell_x = r.x + int(j * self.cell_w / 2)
                    cell_y = r.y + int(i * self.cell_h / 2)
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
        self.bi = Robot().createScreenCapture(self.r.getRect())
        self.parse()

    def getRGB(self, x, y):
        return self.bi.getRGB(x - self.x, y - self.y)

    def paint(self, g):
        super(Overlay, self).paint(g)
        g.setStroke(BasicStroke(2))
        for row in self:
            for cell in row:
                g.setStroke(BasicStroke(2))
                parallelogram = Path2D.Double
                g.setColor(cell.type)
                parallelogram.moveTo(cell.x - self.x, cell.y - self.y + cell.h / 2)
                parallelogram.lineTo(cell.x - self.x + cell.w / 2, cell.y - self.y)
                parallelogram.lineTo(cell.x - self.x, cell.y - self.y - cell.h / 2)
                parallelogram.lineTo(cell.x - self.x - cell.w / 2, cell.y - self.y)
                parallelogram.closePath()
                g.fill(parallelogram)

    def highlight(self, secs):
        self.setLocation(self.x, self.y)
        self.setSize(self.w, self.h)
        self.setVisible(True)
        if secs:
            self.closeAfter(secs)


if __name__ == "__main__":
    grid = Grid(DofusGUI.COMBAT_R, DofusGUI.NBR_V_CELL, DofusGUI.NBR_H_CELL)
    grid.parse()
    grid.highlight(10)
