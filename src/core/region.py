import sys
from time import perf_counter
import cv2
import numpy as np
import pyautogui
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtWidgets import QApplication
from core.utils import capture, isAdjacent
from gui.Overlay import Overlay


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class Location(QPoint):

    def __init__(self, x, y):
        super(QPoint, self).__init__(x, y)

    def click(self):
        pyautogui.click(self.x(), self.y())


class Region(QRect):
    def __init__(self, x, y, w, h):
        super(Region, self).__init__(x, y, w, h)

    def wait(self, template, timeout, threshold=0.7):
        elapsed = 0
        result = None
        start = perf_counter()
        while elapsed < timeout * 1000:
            result = self.findBest(template, threshold)
            if result:
                break
            elapsed = perf_counter() - start
        return result

    def waitVanish(self, timeout, threshold=0.9):
        elapsed = 0
        result = None
        start = perf_counter()
        while elapsed < timeout * 1000:
            result = self.findBest(template, threshold)
            if not result:
                break
            elapsed = perf_counter() - start
        return result

    def click(self):
        pyautogui.click(self.center().x(), self.center().y())
        pass

    def findAll(self, template, threshold=0.8):
        matches = []
        img_rgb = capture(self)
        h, w = template.shape[:-1]
        result = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        bestx, besty = max_loc
        if max_val >= threshold:
            matches.append(Region(self.x() + bestx, self.y() + besty, w, h))
        for dx, dy in zip(*loc[::-1]):
            r = Region(self.x() + dx, self.y() + dy, w, h)
            if not isAdjacent(matches, r):
                matches.append(r)
        return matches

    def findBest(self, template, threshold=0.99):
        img_rgb = capture(self)
        h, w = template.shape[:-1]
        result = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        bestx, besty = max_loc
        if max_val >= threshold:
            return Region(self.x() + bestx, self.y() + besty, w, h)
        else:
            return None

    def highlight(self, secs):
        app = QApplication(sys.argv)
        self.overlay = Overlay()
        self.overlay.highlight(self, secs)
        sys.exit(app.exec_())


if __name__ == "__main__":
    r = Region(1280, 38, 120, 33)
    button_r = Region(1280, 38, 120, 33)
    template = capture(button_r)
    start = perf_counter()
    res = r.findAll(template, threshold=0.9)
    print("it took: ", perf_counter() - start)
    for r in res:
        r.highlight(2)
