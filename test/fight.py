import threading
import traceback
from time import sleep
from core import env
from core.log import Log
import atexit

from core.observer import Observer

log = Log()
lock = threading.Lock()


class Fighter(threading.Thread):
    def __init__(self, spell):
        threading.Thread.__init__(self, name='Fighter')
        self.spell = spell
        self.died = threading.Event()
        self.stopSignal = threading.Event()
        self.combatDetected = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndObs = None

    def run(self):
        log.info('Fighter running')
        while not self.stopSignal.is_set():
            self.waitCombatStarted()
            with lock:
                try:
                    self.combatEndObs = Observer(env.COMBAT_ENDED_POPUP_R,
                                                 env.COMBAT_ENDED_POPUP_P,
                                                 self.onCombatEnded,
                                                 Observer.Mode.APPEAR)
                    self.combatEndObs.start()
                    self.combatAlgo()
                except Exception as e:
                    log.error("Fatal error in combat loop", exc_info=True)
                    self.interrupt()
                    break
                self.combatDetected.clear()
                log.info('combat ended')
        log.info('Goodbye cruel world.')

    def waitCombatStarted(self):
        env.READY_R.waitAppear(env.READY_BUTTON_P)
        env.READY_R.click()
        self.combatDetected.set()
        log.info('Fight started')

    def onCombatEnded(self):
        log.info("Fight ended detected")
        env.END_COMBAT_CLOSE_L.click()
        self.combatEnded.set()
        self.combatEndObs.stop()
        self.stopSignal.set()

    def interrupt(self):
        env.READY_R.stopWait.set()
        self.combatEnded.set()
        self.combatEndObs.stop()
        self.stopSignal.set()

    def combatAlgo(self):
        while not self.combatEnded.wait(0.2):
            pass

    def useSpell(self, target):
        pa_observer = Observer(env.PA_R, mode=Observer.Mode.CHANGE)
        pa_observer.start()
        type(self.spell['shortcut'])
        target.click()
        res = pa_observer.changed.wait(3)
        pa_observer.join()
        return res


def tearDown(fighter):
    fighter.interrupt()
    fighter.join()


if __name__ == "__main__":
    env.focusDofusWindow()
    fighter = Fighter(env.SOURNOISERIE)
    atexit.register(tearDown, fighter)
    fighter.start()
