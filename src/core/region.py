import os
import sys
import threading
import random
from time import perf_counter, sleep
import cv2
import numpy as np
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QColor
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
        env.click(self.x(), self.y())

    def getpixel(self):
        bi = env.capture(Region(self.x(), self.y(), 1, 1))
        return QColor(*bi[0, 0])


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
        while not self.stopWait.is_set() and elapsed < timeout:
            result = self.find(pattern, threshold)
            if result:
                break
            elapsed = perf_counter() - start
        return result

    def waitAny(self, patterns, timeout=FOREVER, threshold=0.7):
        self.stopWait.clear()
        elapsed = 0
        result = None
        start = perf_counter()
        while not self.stopWait.is_set() and elapsed < timeout:
            for pattern in patterns:
                result = self.find(pattern, threshold)
                if result is not None:
                    return pattern
            elapsed = perf_counter() - start
        return result

    def findAnyAll(self, patterns, threshold=0.7, shuffle=False):
        ans = []
        self.capture()
        if shuffle:
            random.shuffle(patterns)
        for pattern in patterns:
            result = self.find(pattern, threshold, capture=False)
            if result:
                ans.append(result)
        return ans

    def findAny(self, patterns, threshold=0.7, shuffle=False):
        self.capture()
        if shuffle:
            random.shuffle(patterns)
        for pattern in patterns:
            result = self.find(pattern, threshold, capture=False)
            if result is not None:
                return result
        return None

    def waitVanish(self, pattern, timeout=FOREVER, threshold=0.9):
        self.stopWait.clear()
        elapsed = 0
        start = perf_counter()
        while not self.stopWait.is_set() and elapsed < timeout:
            result = self.find(pattern, threshold)
            if not result:
                return True
            elapsed = perf_counter() - start
        return False

    def waitChange(self, timeout=FOREVER, nbr_pix=50):
        self.stopWait.clear()
        elapsed = 0
        start = perf_counter()
        initial = env.capture(self)
        while not self.stopWait.is_set() and elapsed < timeout:
            pix_diff = (initial != env.capture(self)).any(axis=2).sum()
            if pix_diff > nbr_pix:
                return True
            elapsed = perf_counter() - start
        return False

    def capture(self):
        self.bi = env.capture(self)
        self.bi = cv2.cvtColor(self.bi, cv2.COLOR_RGB2BGR)
        return self.bi

    def findAll(self, pattern, threshold=0.7, grayscale=True, capture=True):
        matches = []
        if capture:
            self.capture()
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

    def find(self, pattern, threshold=0.7, grayscale=True, capture=True):
        if capture:
            self.capture()
        if grayscale:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_BGR2GRAY)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
        else:
            cvImage = cv2.cvtColor(self.bi, cv2.COLOR_RGB2BGR)
            pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        h, w = pattern.shape[:2]
        result = cv2.matchTemplate(cvImage, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        bestx, besty = max_loc
        if max_val >= threshold:
            return Region(self.x() + bestx, self.y() + besty, w, h)
        else:
            return None

    def highlight(self, secs):
        app = QApplication(sys.argv)
        self.overlay = overlay.Overlay()
        self.overlay.highlight(self, secs)
        app.exec_()

    def click(self):
        env.click(self.center().x(), self.center().y())

    def getpixel(self, x, y):
        return tuple(self.bi[y, x])

    def hover(self):
        env.move(self.center().x(), self.center().y())

    def nearBy(self, w, h):
        return Region(self.center().x() - w / 2, self.center().y() - h / 2, w, h)


if __name__ == "__main__":
    from core import dofus
    from core.grid import Grid

    # app = QApplication(sys.argv)
    env.focusDofusWindow()
    s = perf_counter()
    ans, pattern = dofus.COMBAT_R.findAny(dofus.mobs, threshold=0.7)
    print(f"took {perf_counter() - s}")
    print(ans)
    if ans:
        ans.highlight(1)

    cv2.imshow("pattern", pattern)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()
    # button_r = tst.r
    # button_r.capture()
    # pix = button_r.getpixel(0, 0)
    # while True:
    #     if dofus.MY_TURN_CHECK_L.getpixel() == dofus.MY_TURN_C:
    #         print('Bot turn started')
    #         break
    # not my turn color (0 144 122 255)
    # my turn color (0 242 205 255)
    # s = perf_counter()
    # res = myTurnCheckL.getpixel()
    # print(perf_counter() - s)
    # print(res)
    # sleep(1)
    # env.focusIDEWindow()
    # start = perf_counter()
    # template = cv2.imread(os.path.join(env.test_patterns_dir, tst.p))
    # res = button_r.findAll(template)
    # elapsed = perf_counter() - start
    # print("detection took: ", elapsed)
    #
    # print("r: ", res)
    # if res:
    #     env.focusDofusWindow()
    #     for r in res:
    #         r.highlight(2)
    #         r.overlay.highlightEnded.connect(env.focusIDEWindow)
    # else:
    # env.focusIDEWindow()
