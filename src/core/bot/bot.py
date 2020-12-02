import logging
import os
import re
import threading
from time import perf_counter, sleep
import cv2
import numpy as np
import pyautogui
import pytesseract
from core import Observer, dofus, env, utils, Region


class Pattern(dict):
    def __init__(self, kind, path_to_pattern, id):
        super(Pattern, self).__init__({
            'kind': kind,
            'id': id,
            'bi': cv2.imread(path_to_pattern)
        })


class Bot(threading.Thread):

    def __init__(self, workdir, name="Bot"):
        super(Bot, self).__init__(name=name)
        self.killsig = threading.Event()
        self.combatStarted = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndReached = threading.Event()
        self.lock = threading.Lock()
        self.disconnected = threading.Event()
        self.connected = threading.Event()
        self.name = name
        self.dead = False
        self.workdir = workdir
        self.disconnectedObs = Observer(dofus.CONNECT_R,
                                        dofus.DISCONNECTED_BOX_P,
                                        self.reconnect,
                                        Observer.Mode.APPEAR,
                                        rate=1 / 5)
        self.patternsDir = os.path.join(self.workdir, 'patterns')
        self.patterns = {}
        self.loadPatterns()
        self.resourcesToFarm = []
        self.mapChangeTimeOut = 7.6

    def loadPatterns(self):
        for patternDir in os.listdir(self.patternsDir):
            self.patterns[patternDir] = []
            fpath = os.path.join(self.patternsDir, patternDir)
            for path_to_img, fn in utils.iterPatternsImg(fpath):
                self.patterns[patternDir].append(Pattern(patternDir, path_to_img, fn))

    def interrupt(self):
        self.killsig.set()
        self.disconnectedObs.stop()

    def reconnect(self):
        logging.info("Disconnected popup appeared!")
        self.disconnected.set()
        self.connected.clear()
        sleep(4)
        dofus.CLOSE_DISCONNECTED_BOX_L.click()
        dofus.CONNECT_R.waitVanish(dofus.DISCONNECTED_BOX_P)
        dofus.RECONNECT_BUTTON_R.click()
        sleep(4)
        if self.waitMapCoords(99999):
            self.disconnected.clear()
            self.connected.set()

    @staticmethod
    def parseMapCoords():
        image = env.capture(dofus.MAP_COORDS_R)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        low_bound = np.array([160, 60, 0])
        upper_bound = np.array([255, 255, 255])

        bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mask = cv2.inRange(bgr_img, low_bound, upper_bound)
        result = cv2.bitwise_and(gray, gray, mask=mask)
        result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV)[1]
        newShape = (int(dofus.MAP_COORDS_R.width() * 10), int(dofus.MAP_COORDS_R.height() * 10))
        result = cv2.resize(result, newShape)
        result = cv2.blur(result, (7, 7))
        text = pytesseract.image_to_string(result, config='--psm 6')

        print(text)
        res = re.findall("(-?\d+)", text)
        if res:
            return int(res[0]), int(res[1])
        else:
            return None

    def waitMapCoords(self, timeout=5):
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            if self.parseMapCoords():
                return True
            sleep(0.2)
        return False

    @staticmethod
    def fullPods():
        return dofus.FULL_POD_CHECK_L.getpixel() == dofus.FULL_POD_COLOR

    @staticmethod
    def shiftClick(tgt):
        pyautogui.keyDown('shift')
        sleep(0.1)
        tgt.click()
        sleep(0.1)
        pyautogui.keyUp('shift')
        sleep(0.1)
        dofus.OUT_OF_COMBAT_R.hover()

    def collect(self, spot, timeout=7):
        tgt = spot['region']

        with self.lock:
            self.shiftClick(tgt)

        if spot['pattern']['kind'] == 'poisson' or spot['pattern']['kind'] == 'poissonMoyen':
            sleep(1)
            if not tgt.waitChange(5):
                return False
            sleep(1)
            res = tgt.waitChange(2.5)
        else:
            res = dofus.SLOTS_R.waitChange(timeout)

        if self.combatStarted.is_set():
            self.combatEnded.wait()

        if self.disconnected.is_set():
            self.connected.wait()

        self.checkPopup()

        return res

    def harvest(self):
        pass

    @staticmethod
    def checkPopup():
        m = dofus.LVL_UP_INFO_R.find(dofus.CLOSE_POPUP_P)
        if m:
            m.click()

