import logging
import re
import threading
from time import perf_counter
import numpy as np
import cv2
from pytesseract import pytesseract
from core.exceptions import *
from core import env, dofus


class Walk:

    def __init__(self, parent=None):
        self.killsig = threading.Event()
        self.lock = threading.Lock()
        self.coordinates = None
        self.lastMap = None
        self.parent = parent
        if self.parent:
            self.killsig = parent.killsig
        else:
            self.killsig = threading.Event()

    @staticmethod
    def parseMapCoords():
        image = env.capture(dofus.MAP_COORDS_R)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        low_bound = np.array([228, 220, 220])
        upper_bound = np.array([255, 230, 255])
        bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mask = cv2.inRange(bgr_img, low_bound, upper_bound)
        result = cv2.bitwise_and(gray, gray, mask=mask)
        result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV)[1]
        text = pytesseract.image_to_string(result, config='--psm 6')
        res = re.findall("(-?\d+),?(-?\d+)", text)
        if res:
            return int(res[0][0]), int(res[0][1])
        else:
            return None

    def updateCoords(self):
        self.coordinates = self.parseMapCoords()
        if self.coordinates:
            return self.coordinates
        else:
            raise ParseMapCoordsFailed(f"Enable to parse map coords")

    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            with self.lock:
                currx, curry = self.updateCoords()
                dstx, dsty = currx + direction[0], curry + direction[1]
                dofus.mapChangeLoc[direction].click()
                dofus.COMBAT_R.hover()
            if self.waitMapChange(dstx, dsty):
                self.lastMap = (currx, curry)
                return True
            nbr_fails += 1
        return False

    def waitMapChange(self, x, y, timeout=8):
        logging.debug(f"Current map coords: {self.coordinates}")
        logging.debug(f"Changing map to destination ({x}, {y})")
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            with self.lock:
                if self.updateCoords() == (x, y):
                    logging.debug(f"Change map took {perf_counter() - s}")
                    return True
        return False

    def moveToZone(self, zone):
        exclude = set()
        while not self.killsig.is_set():
            path = zone.pathToEntry(self.coordinates, exclude)
            for x, y in path:
                currx, curry = self.coordinates
                direction = x - currx, y - curry
                if not self.changeMap(direction):
                    exclude.add((x, y))
                    break
                exclude = set()
            return True
        return False


