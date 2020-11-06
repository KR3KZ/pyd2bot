import logging
import re
import threading
from time import perf_counter, sleep
import numpy as np
import cv2
from pytesseract import pytesseract
from core.exceptions import *
from core.fighter import Fighter
from core.observer import Observer
from core import env, dofus


class Bot(threading.Thread):

    def __init__(self, zone, spell, save_path, name):
        threading.Thread.__init__(self, name=name)
        self.killsig = threading.Event()
        self.stopRetry = threading.Event()
        self.disconnected = threading.Event()
        self.lock = threading.Lock()
        self.fighter_thread = Fighter(spell, parent=self)
        self.harvestZone = zone
        self.currMapCoords = None
        self.disconnectedObs = Observer(dofus.RECONNECT_BUTTON_R,
                                        dofus.DISCONNECTED_BOX_P,
                                        self.reconnect,
                                        Observer.Mode.APPEAR)
        self.save_path = save_path
        self.last_map = None

    def harvestCombats(self, mobs_patterns):
        farmed = 0
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < 3:
            logging.debug("Searching for mobs group...")
            tgt = dofus.COMBAT_R.findAny(mobs_patterns, threshold=0.75, shuffle=True)
            if tgt:
                logging.debug("I found a mob group")
                if self.enterCombat(tgt):
                    self.fighter_thread.combatEnded.wait()
                    farmed += self.fighter_thread.mobs_killed
                    if self.fighter_thread.died:
                        logging.debug("Bot died during combat!")
                else:
                    nbr_fails += 1
            else:
                logging.debug("No mobs found")
                break
        return farmed

    def enterCombat(self, tgt, timeout=5):
        with self.lock:
            tgt.click()
            logging.debug("Clicked on mobs group")
        s = perf_counter()
        if self.fighter_thread.combatDetected.wait(timeout):
            logging.info(f"Enter combat took: {perf_counter() - s}")
            return True
        logging.debug("Couldn't open combat!")
        return False

    def interrupt(self):
        self.fighter_thread.interrupt()
        self.disconnectedObs.stop()
        self.killsig.set()
        self.stopRetry.set()
        self.harvestZone.saveTo(self.save_path)

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

    def updateMapCoords(self):
        self.currMapCoords = self.parseMapCoords()
        if self.currMapCoords:
            return self.currMapCoords
        else:
            raise ParseMapCoordsFailed(f"Enable to parse map coords")

    def moveTo(self, direction, timeout=6.4, nbr_retries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < nbr_retries:
            with self.lock:
                currx, curry = self.updateMapCoords()
                logging.info(f"Current map coords: {self.currMapCoords}")
                dstx, dsty = currx + direction[0], curry + direction[1]
                logging.debug(f"Changing map to destination {(dstx, dsty)}")
                dofus.mapChangeLoc[direction].click()
                dofus.COMBAT_R.hover()
            s = perf_counter()
            while not self.killsig.is_set() and perf_counter() - s < timeout:
                with self.lock:
                    if self.updateMapCoords() == (dstx, dsty):
                        self.last_map = currx, curry
                        logging.info(f"Change map took {perf_counter() - s}")
                        return True
            nbr_fails += 1
        return False

    def moveToZone(self):
        exclude = set()
        while not self.killsig.is_set():
            path = self.harvestZone.pathToEntry(self.currMapCoords, exclude)
            for x, y in path:
                currx, curry = self.currMapCoords
                direction = x - currx, y - curry
                if not self.moveTo(direction):
                    exclude.add((x, y))
                    break
                exclude = set()
            return True

    def reconnect(self):
        logging.info("Disconnected popup appeared!")
        self.disconnected.set()
        dofus.CLOSE_DISCONNECTED_BOX_L.click()
        dofus.RECONNECT_BUTTON_R.waitVanish(dofus.DISCONNECTED_BOX_P)
        dofus.RECONNECT_BUTTON_R.click()
        dofus.PLAY_GAME_BUTTON_R.waitAppear(dofus.PLAY_GAME_BUTTON_P)
        dofus.PLAY_GAME_BUTTON_R.click()
        while not self.parseMapCoords():
            sleep(1)
        self.disconnected.clear()

    def insideZone(self):
        return self.harvestZone.inside(*self.currMapCoords)