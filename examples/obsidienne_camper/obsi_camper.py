import random
import threading
from time import sleep
import cv2
from core import utils
from core.bot import Fighter
from core import env, Region

env.focusDofusWindow()

rcenter = Region(1185, 466, 80, 71)
rup = Region(1066, 538, 34, 19)
rout = Region(1126, 264, 41, 40)

resource_r = Region(1166, 338, 127, 118)

spots = [Region(1166, 339, 40, 73),
         Region(1215, 362, 32, 67),
         Region(1255, 385, 38, 64)]

empty_spot_ptrn = [
    cv2.imread(f"empty_spot{idx}.png", cv2.IMREAD_GRAYSCALE) for idx in range(3)
]

am = {
    "range": 2,
    "nbr": 2,
    "shortcut": "r"
}


class AntiSaveScreen(threading.Thread):

    def __init__(self, region):
        super(AntiSaveScreen, self).__init__()
        self.region = region
        self.killsig = threading.Event()

    def run(self):
        while not self.killsig.is_set():
            sleep(60)
            env.click(self.region.center().x() + int((random.random() - 0.5) * 10),
                      self.region.center().y() + int((random.random() - 0.5) * 10))


class Camper(Fighter):

    def __init__(self):
        super(Camper, self).__init__(spell=am)
        self.noss = AntiSaveScreen(rout)

    def run(self):
        super(Camper, self).run()
        self.noss.start()
        for frame in resource_r.stream(9999):
            for idx, spot in enumerate(spots):
                if self.combatStarted.is_set():
                    self.combatEnded.wait()
                x, y, w, h = spot.getRect()
                rx = x - resource_r.x()
                ry = y - resource_r.y()
                spot_img = frame[ry:ry + h, rx:rx + w]
                if not utils.areSame(spot_img, empty_spot_ptrn[idx]):
                    spot.click()
                    rout.hover()
                    sleep(2)
                    break

    def interrupt(self):
        super(Camper, self).interrupt()
        self.noss.killsig.set()


Camper().start()
