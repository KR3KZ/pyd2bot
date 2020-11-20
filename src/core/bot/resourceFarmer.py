import datetime
import logging
import os
from threading import Timer
from time import perf_counter, sleep
import pyautogui
import yaml
from core.bot import Fighter
from core import dofus, Region


class ResourceFarmer(Fighter):

    def __init__(self, zone, spell, patterns, save_path, name):
        super(ResourceFarmer, self).__init__(spell, name=name)
        self.resource_patterns = [[_, 0] for _ in patterns]
        self.nbr_no_farm = {}
        self.cache = {}
        self.save_path = save_path
        self.zone = zone
        self.tmpIgnore = []

    def run(self):
        super(ResourceFarmer, self).run()
        s = perf_counter()
        self.loadCache()
        self.updatePos()

        while not self.killsig.is_set():
            try:
                if dofus.FULL_POD_CHECK_L.getpixel() == dofus.FULL_POD_COLOR:
                    self.discharge()
                    sleep(20)
                    self.updatePos()

                if self.currPos not in self.zone:
                    self.moveToZone(self.zone)
                self.updatePos()

                self.tmpIgnore.append(self.currPos)
                Timer(1.5 * 60.0, self.onTimer).start()
                self.resource_patterns.sort(key=lambda it: it[1])

                result = self.harvestResources([p for p, s in self.resource_patterns])

                self.zone[self.currPos]['farmed'] += result['farmed']

                for idx, score in result['matched'].items():
                    self.resource_patterns[idx][1] += score

                self.randomWalk(self.zone)

            except Exception as e:
                print(e)
                if self.disconnected.wait(10):
                    self.connected.wait(30)
                else:
                    logging.error("Fatal error!", exc_info=True)
                    self.interrupt()
                    break

        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logging.info(f"farmed in {total_time}.")
        logging.info("Goodbye cruel world!")

    def discharge(self):
        pyautogui.press(dofus.RAPPEL_POTION_SHORTCUT)
        sleep(2)
        self.updatePos()
        self.changeMap(dofus.RIGHT)
        sleep(2)
        Region(1067, 440, 25, 43).click()  # enter bank click
        dofus.BANK_MAN_R.waitAppear(dofus.BANK_MAN_P)
        dofus.BANK_MAN_R.click()
        dofus.BANK_MAN_TALK_R.waitAppear(dofus.BANK_MAN_TALK_P)
        Region(771, 737, 272, 40).click()  # click first choice
        dofus.INV_OPEN_R.waitAppear(dofus.INVENTAIRE_P)
        Region(1469, 142, 29, 26).click()
        sleep(1)
        Region(1248, 138, 34, 33).click() # click transfer
        sleep(1)
        Region(1276, 178, 222, 23).click()  # click transfer visible
        dofus.INV_FIRST_SLOT_R.waitAppear(dofus.EMPTY_SLOT_INV_P)
        Region(1526, 109, 52, 22).click() # close
        sleep(1)
        pyautogui.press("h")
        sleep(2)
        havre_sac_zaap_r = Region(525, 380, 79, 54)
        havre_sac_zaap_r.click()
        sleep(2)
        # zaap_open_r = Region(645, 679, 638, 115)
        # zaap_open_p = "zaap_open_p.png"
        zaap_choices_r = Region(641, 268, 552, 461)
        res = zaap_choices_r.find(dofus.COIN_BOUF_ZAAP_P)
        res.click()
        sleep(0.08)
        res.click()

    def onTimer(self):
        if self.tmpIgnore:
            self.tmpIgnore.pop(0)

    def randomWalk(self, zone):
        while not self.killsig.is_set():
            dst, direction = zone[self.currPos].randDirection(self.lastPos, ignore=self.tmpIgnore)
            if self.changeMap(direction, max_tries=2):
                return True
            else:
                zone[self.currPos].exclude(self.lastPos, dst)

    def interrupt(self):
        self.saveCache()
        super(ResourceFarmer, self).interrupt()

    def loadCache(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r') as f:
                self.cache = yaml.load(f, Loader=yaml.FullLoader)

    def harvestResources(self, resource_patterns, max_farm=15, shuffle=False):
        """
        Look for resource patterns and try to collect them.
        :param resource_patterns: list of images
        :param max_farm: max number of clicks on resource
        :param shuffle: if you want to shuffle resource patterns before matching
        :return: nbr of resource farmed and the matched patterns with nbr of times matched
        """
        result = {
            "farmed": 0,
            "matched": {}
        }
        ignore = []
        logging.debug("Searching for resources...")
        nbr_collected = 0
        while not self.killsig.is_set() and nbr_collected < max_farm:
            self.resource_patterns.sort(key=lambda it: it[1])
            tgt, idx = dofus.COMBAT_R.findAny(resource_patterns, threshold=0.85, shuffle=shuffle)
            if tgt and tgt not in ignore:
                ignore.append(tgt)
                if idx not in result['matched']:
                    result['matched'][idx] = 0
                result['matched'][idx] += 1
                self.collect(tgt)
                if self.combatStarted.is_set():
                    self.combatEnded.wait()
                m = dofus.LVL_UP_INFO_R.find(dofus.CLOSE_POPUP_P)
                if m:
                    m.click()
                nbr_collected += 1
            else:
                break
        return result

    def collect(self, tgt):
        with self.lock:
            pyautogui.keyDown('shift')
            sleep(0.1)
            tgt.click()
            sleep(0.1)
            pyautogui.keyUp('shift')
            sleep(0.1)
            dofus.OUT_OF_COMBAT_R.hover()
            dofus.SLOTS_R.waitChange(8)

    def saveCache(self):
        with open(self.save_path, 'w') as f:
            yaml.dump(self.cache, f)
