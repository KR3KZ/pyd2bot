import os
import sys
import threading
from time import perf_counter, sleep
import cv2
import numpy as np
import pyautogui
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtWidgets import QApplication
from core.utils import isAdjacent
import gui.Overlay as overlay
import core.env as env

FOREVER = 60 * 60 * 24


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class Location(QPoint):
    def __init__(self, x, y):
        super(Location, self).__init__(x, y)

    def click(self):
        pyautogui.click(self.x(), self.y())


class Region(QRect):

    def __init__(self, x, y, w, h):
        super(Region, self).__init__(x, y, w, h)
        self.bi = None
        self.stopWait = threading.Event()

    def waitAppear(self, pattern, timeout=FOREVER, threshold=0.7):
        self.stopWait.clear()
        elapsed = 0
        result = None
        start = perf_counter()
        while not self.stopWait.is_set() and elapsed < timeout * 1000:
            result = self.find(pattern, threshold)
            if result:
                break
            elapsed = perf_counter() - start
        return result

    def waitVanish(self, pattern, timeout=FOREVER, threshold=0.9):
        self.stopWait.clear()
        elapsed = 0
        result = None
        start = perf_counter()
        while elapsed < timeout * 1000:
            result = self.find(pattern, threshold)
            if not result:
                break
            elapsed = perf_counter() - start
        return result

    def waitChange(self, timeout=FOREVER, threshold=0.9):
        self.bi = env.capture(self)
        return self.waitVanish(self.bi, timeout, threshold)

    def findAll(self, pattern, threshold=0.7, grayscale=True):
        matches = []
        self.bi = env.capture(self)
        if grayscale:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_BGR2GRAY)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
        else:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_RGB2BGR)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        h, w = pattern.shape[:2]
        result = cv2.matchTemplate(cvImage, pattern, cv2.TM_CCOEFF_NORMED)
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

    def find(self, pattern, threshold=0.7, grayscale=True):
        self.bi = env.capture(self)
        if grayscale:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_BGR2GRAY)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
        else:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_RGB2BGR)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        h, w = pattern.shape
        result = cv2.matchTemplate(cvImage, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        bestx, besty = max_loc
        if max_val >= threshold:
            return Region(self.x() + bestx, self.y() + besty, w, h)
        else:
            return None

    def highlight(self, secs):
        self.overlay = overlay.Overlay()
        self.overlay.highlight(self, secs)

    def click(self):
        pyautogui.click(self.center().x(), self.center().y())


if __name__ == "__main__":
    import tests as tst

    app = QApplication(sys.argv)
    env.focusDofusWindow()
    button_r = tst.r

    start = perf_counter()
    template = cv2.imread(os.path.join(env.test_patterns_dir, tst.p))
    res = button_r.findAll(template)
    elapsed = perf_counter() - start
    print("detection took: ", elapsed)

    print("r: ", res)
    if res:
        for r in res:
            env.focusDofusWindow()
            r.highlight(2)
            r.overlay.highlightEnded.connect(env.focusIDEWindow)
    else:
        env.focusIDEWindow()
    sys.exit(app.exec_())
