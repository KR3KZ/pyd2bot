import logging
import re
import threading
from time import perf_counter, sleep
import cv2
import numpy as np
import pytesseract
from core import Observer, dofus, env


class Bot(threading.Thread):

    def __init__(self, name="Bot"):
        super(Bot, self).__init__(name=name)
        self.killsig = threading.Event()
        self.combatStarted = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndReached = threading.Event()
        self.lock = threading.Lock()
        self.disconnected = threading.Event()
        self.connected = threading.Event()
        self.dead = False
        self.disconnectedObs = Observer(dofus.CONNECT_R,
                                        dofus.DISCONNECTED_BOX_P,
                                        self.reconnect,
                                        Observer.Mode.APPEAR,
                                        rate=1 / 5)

    def run(self):
        self.disconnectedObs.start()

    def interrupt(self):
        self.killsig.set()
        self.disconnectedObs.stop()

    def reconnect(self):
        logging.info("Disconnected popup appeared!")
        self.disconnected.set()
        self.connected.clear()
        dofus.CLOSE_DISCONNECTED_BOX_L.click()
        dofus.CONNECT_R.waitVanish(dofus.DISCONNECTED_BOX_P)
        dofus.RECONNECT_BUTTON_R.click()
        dofus.PLAY_GAME_BUTTON_R.waitAppear(dofus.PLAY_GAME_BUTTON_P)
        dofus.PLAY_GAME_BUTTON_R.click()
        if self.waitMapCoords(8):
            self.disconnected.clear()
            self.connected.set()

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

    def waitMapCoords(self, timeout=5):
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            if self.parseMapCoords():
                return True
            sleep(0.2)
        return False