import pyautogui
from PyQt5.QtCore import QPoint, QRect, QPointF
from time import perf_counter

from PyQt5.QtGui import QPolygon, QRegion, QColor


class Location(QPoint):

    def __init__(self, x, y):
        super(QPoint, self).__init__(x, y)

    def click(self):
        pyautogui.click(self.x(), self.y())


class Region(QRect):
    def __init__(self, x, y, w, h):
        super(Region, self).__init__(x, y, w, h)

    def exists(self, img, secs=3):
        # TODO
        pass

    def click(self):
        pyautogui.click(self.x() + self.width() / 2, self.y() + self.height() / 2)
        pass

print(QColor(255,0,0).getRgb())
# start = perf_counter()
# bi = pyautogui.screenshot(region=(831, 232, 70, 33))
# rgb_tuple = bi.getpixel((10, 10))
# print(QColor(*rgb_tuple))
# print('it took: ', perf_counter() - start)

# r = QRect(0, 0, 100, 100)
# print(r.getRect())

# g = Grid(QRect(0, 0, 10, 10))
# print(g.parse())
