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
from gui import Overlay
import core.env as env

FOREVER = 60 * 60 * 24 * 1.


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


def withTimeOut(fn):
    def wrapped(self, *args, timeout=FOREVER, rate=3):
        self.stopWait.clear()
        start = perf_counter()
        while not self.stopWait.is_set() and perf_counter() - start < timeout:
            s = perf_counter()
            r = fn(self, *args)
            if r:
                return r
            rest = (1 / rate) - perf_counter() + s
            sleep(rest if rest > 0 else 0)
        return None, None
    return wrapped


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

    @withTimeOut
    def waitAppear(self, pattern, threshold=0.7):
        match = self.find(pattern, threshold)
        if match:
            return match

    @withTimeOut
    def waitAny(self, patterns, threshold=0.7):
        match, idx = self.findAny(patterns, threshold)
        if match:
            return match, idx

    @withTimeOut
    def waitVanish(self, pattern, threshold=0.9):
        match = self.find(pattern, threshold)
        if not match:
            return pattern, match

    def waitChange(self, timeout=FOREVER, nbr_pix=50):
        self.stopWait.clear()
        start = perf_counter()
        initial = env.capture(self)
        while not self.stopWait.is_set() and perf_counter() - start < timeout:
            pix_diff = (initial != env.capture(self)).any(axis=2).sum()
            if pix_diff > nbr_pix:
                return True
            sleep(0.01)
        return False

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
            match = self.find(pattern, threshold, capture=False)
            if match:
                return match, idx
        return None, None

    def waitAnimationEnd(self, timeout=FOREVER):
        self.stopWait.clear()
        lookup_int = 4
        clip = collections.deque()
        for frame in self.stream(timeout):
            if len(clip) > lookup_int:
                if utils.inMotion(clip):
                    return True
                clip.popleft()
            clip.append(frame)
            sleep(0.17)
        return False

    def capture(self, gray=False):
        self.bi = env.capture(self)
        if gray:
            self.bi = cv2.cvtColor(self.bi, cv2.COLOR_RGB2GRAY)
        else:
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
        self.overlay = Overlay()
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



