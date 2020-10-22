import atexit
import sys
import threading
import traceback
from functions import *
import constants as cnst
import os
lock = threading.Lock()

SRC_DIR = "C:\Users\khalid.majdoub\Documents"
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)


class Fighter(threading.Thread):
    def __init__(self, nbr_pm, spell, scan_rate=3):
        threading.Thread.__init__(self)
        self.scan_rate = scan_rate
        self.spell = spell
        self.nbr_pm = nbr_pm
        self.isDead = threading.Event()
        self.stopSignal = threading.Event()
        self.combatDetected = threading.Event()
        self.combatEnded = threading.Event()

    def run(self):
        logger.debug('fighter running')

        while not self.stopSignal.is_set():
            match = None
            while not self.stopSignal.is_set():
                try:
                    with lock:
                        match = cnst.READY_R.wait(cnst.READY_P, 1. / self.scan_rate)
                    self.combatDetected.set()
                    logger.debug('********AGRO DETECTED********')
                    break
                except:
                    pass

            if self.stopSignal.is_set(): break
            with lock:
                match.click()
                try:
                    self.combatAlgo()
                except Exception as e:
                    logger.debug(traceback.print_exc())
                self.combatDetected.clear()
                logger.debug('combat ended')
                self.combatEnded.set()
                wait(3)
        logger.debug('fighter stopped')

    def interrupt(self):
        cnst.PA_R.stopObserver()
        cnst.END_R.stopObserver()
        self.stopSignal.set()

    def waitTurn(self):
        logger.debug('waiting bot turn')
        while not self.stopSignal.is_set():
            try:
                cnst.YOUR_TURN_R.wait(cnst.YOUR_TURN_P, 0.33)
                break
            except:
                pass

    def happened(self, event, signal, rep=False):
        signal.set()
        if rep:
            event.repeat()

    def combatAlgo(self):
        logger.debug('combat started')
        nbr_retry = 0
        paChanged = threading.Event()
        self.combatEnded.clear()
        cnst.PA_R.onChange(lambda e: self.happened(e, paChanged, True))
        cnst.PA_R.observeInBackground(FOREVER)

        while not self.stopSignal.is_set():
            myTurn = False
            spell_nbr = self.spell['nbr']
            pm = self.nbr_pm

            self.waitTurn()
            myTurn = True

            if self.stopSignal.is_set():
                return

            me_pos = cnst.COMBAT_R.findBest(cnst.MAP_R, cnst.ME_P)
            mobs_pos = cnst.COMBAT_R.findBestList(cnst.MAP_R, cnst.MOB_P)

            nbr_retry = 0
            try:
                logger.debug('playing turn')
                tgt_pos, me_tgt_dist = selectTarget(mobs_pos, me_pos)
                tgt_color = tgt_pos.getColor()
                logger.debug('distance from target = ' + str(me_tgt_dist))
                while not self.stopSignal.is_set() and spell_nbr > 0:
                    paChanged.clear()
                    if me_tgt_dist < self.spell['range']:
                        if me_tgt_dist > 2:
                            useSpell("d", tgt_pos)
                        else:
                            useSpell(self.spell["shortcut"], tgt_pos)
                        if paChanged.is_set():
                            spell_nbr -= 1
                            wait(.8)
                            if tgt_pos.getColor() != tgt_color:
                                tgt_pos, me_tgt_dist = selectTarget(mobs_pos, me_pos)
                        else:
                            logger.debug("can't hit target, moving...")
                            me_pos, me_tgt_dist, pm = moveTowardsTarget(me_pos[0], tgt_pos, min(pm, me_tgt_dist - 1))
                    else:
                        logger.debug('target not in range')
                        me_pos, me_tgt_dist, pm = moveTowardsTarget(me_pos[0], tgt_pos, pm)
            except Exception as e:
                logger.debug(e)
                pass

            if cnst.END_R.exists(cnst.END_COMBAT_P, 1):
                cnst.END_R.click(cnst.END_COMBAT_P)
                cnst.PA_R.stopObserver()
                if not myTurn:
                    self.isDead.set()
                return

            else:
                meR = getNearBy(me_pos[0], 5 * cnst.CELL_W, 5 * cnst.CELL_H)
                type("f")


class Farmer(threading.Thread):
    def __init__(self, resource_pattern, src_path, fighter_thread, nbr_cycles=1, start_step=0, max_pods=18000,
                 min_pods=2000):
        threading.Thread.__init__(self)
        self.stop_signal = threading.Event()
        self.resource_pattern = resource_pattern
        self.src_path = src_path
        self.curr_step = start_step
        self.nbr_cycles = nbr_cycles
        self.current_tgt = None
        self.stop_signal = threading.Event()
        self.fighter_thread = fighter_thread
        self.max_pods = 2071
        self.farm_path = loadFarmPath(self.src_path)
        self.curr_pods = min_pods

    def run(self):
        self.fighter_thread.start()
        path_length = len(self.farm_path)
        cycle = 0
        pods = 0
        while not self.stop_signal.is_set() and cycle < self.nbr_cycles:

            while not self.stop_signal.is_set() and self.curr_step < path_length:

                if self.fighter_thread.combatDetected.is_set():
                    pods += 150
                    logger.debug('waiting for fighter to end...')
                    self.fighter_thread.combatEnded.wait()
                    self.fighter_thread.combatEnded.clear()
                    if self.fighter_thread.isDead.is_set():
                        self.fighter_thread.isDead.clear()
                        break

                logger.debug('step number ' + str(self.curr_step) + ' ...')
                rtype, rregion = self.farm_path[self.curr_step]
                self.curr_step += 1

                if rtype != 'mapChange':
                    collectResource(self.resource_pattern[rtype], rregion)

                else:
                    logger.debug('changing map...')
                    with lock:
                        changeMap()
                    logger.debug('map changed')

            if not self.stop_signal.is_set():
                cycle += 1
                self.curr_step = 0
                sleep(9)
                with lock:
                    useRappelPotion()
                sleep(2)
                logger.debug('cycle number' + str(cycle) + 'ended')

        self.fighter_thread.interrupt()
        logger.debug('farmer stopped')

    def interrupt(self):
        self.stop_signal.set()


def cleanUp():
    fighter_thread.interrupt()
    # farmer.interrupt()


if __name__ == "__main__":
    atexit.register(cleanUp)
    farming_path = "dofus_bot.sikuli\\frighost_fish.sikuli\\path01.txt"
    farm_path = os.path.join(SRC_DIR, farming_path)
    Settings.MoveMouseDelay = 0.3
    Settings.ClickDelay = 0.1
    Settings.observeScanRate = 3
    fighter_thread = Fighter(nbr_pm=4, nbr_spell=2, spell_range=7, scan_rate=3)
    # farmer  = Farmer(pattern, farm_path, fighter_thread, start_step =0, nbr_cycles = 5)
    # farmer.start()
    # farmer.join()
    fighter_thread.start()
    fighter_thread.join()
