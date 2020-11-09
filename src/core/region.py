import collections
import sys
import threading
import random
from time import perf_counter, sleep
import cv2
import numpy as np
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from core import utils
import gui.Overlay as overlay
import core.env as env

FOREVER = 60 * 60 * 24 * 1.


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

    def waitAppear(self, pattern, timeout=FOREVER, threshold=0.7, rest_time=0):
        self.stopWait.clear()
        elapsed = 0
        result = None
        start = perf_counter()
        while not self.stopWait.is_set() and elapsed < timeout:
            result = self.find(pattern, threshold)
            if result:
                break
            sleep(rest_time)
            elapsed = perf_counter() - start
        return result

    def waitAny(self, patterns, timeout=FOREVER, threshold=0.7):
        self.stopWait.clear()
        elapsed = 0
        start = perf_counter()
        while not self.stopWait.is_set() and elapsed < timeout:
            for pattern in patterns:
                match = self.find(pattern, threshold)
                if match:
                    return pattern, match
            elapsed = perf_counter() - start
        return None, None

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
        for idx, pattern in enumerate(patterns):
            target = self.find(pattern, threshold, capture=False)
            if target is not None:
                return target, idx
        return None, None

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

    def waitAnimationEnd(self, timeout=FOREVER):
        self.stopWait.clear()
        lookup_int = 5
        clip = collections.deque()
        for frame in self.stream(timeout):
            if len(clip) > lookup_int:
                if utils.inMotion(clip):
                    return True
                clip.popleft()
            clip.append(frame)
            sleep(0.2)
        return False

    def capture(self):
        self.bi = env.capture(self)
        self.bi = cv2.cvtColor(self.bi, cv2.COLOR_RGB2BGR)
        return self.bi

    def stream(self, interval=FOREVER):
        s = perf_counter()
        while perf_counter() - s < interval:
            yield cv2.cvtColor(env.capture(self), cv2.COLOR_RGB2GRAY)

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
            if not utils.isAdjacent(matches, r):
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



