import logging
import threading
from core import Observer, dofus
from core.bot import Walker


class Bot(Walker):

    def __init__(self, spell, name="Bot"):
        super(Bot, self).__init__(name)
        self.spell = spell
        self.dead = threading.Event()
        self.killsig = threading.Event()
        self.combatStarted = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndReached = threading.Event()
        self.killsig = threading.Event()
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
        while not self.parseMapCoords():
            pass
        self.disconnected.clear()
        self.connected.set()
