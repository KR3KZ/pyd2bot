import java.awt.Color as Color
import threading
import atexit
import logging
import traceback
import sys, time

lock = threading.Lock()

src_dir = "c:\Users\kmajdoub\Desktop"
if not src_dir in sys.path:
    sys.path.append(src_dir)
import constants as cnst
from functions import *


class Fighter(threading.Thread):
    def __init__(self, region, pattern, pmNbr, spellNbr, spellRange, scanRate=3):
        threading.Thread.__init__(self)
        self.pattern = pattern
        self.region = region
        self.scanRate = scanRate
        self.spellNbr = spellNbr
        self.pmNbr = pmNbr
        self.spellRange = spellRange
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
                        match = self.region.wait(self.pattern, 1. / self.scanRate)
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
        logger.debug('fighter stoped')

    def interrupt(self):
        PA_R.stopObserver()
        END_R.stopObserver()
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
        if rep: event.repeat()

    def combatAlgo(self):
        logger.debug('combat started')
        nbrEchec = 0
        paChanged = threading.Event()
        self.combatEnded.clear()
        PA_R.onChange(lambda e: self.happened(e, paChanged, True))
        PA_R.observeInBackground(FOREVER)
        meR = MAP_R
        while not self.stopSignal.is_set():
            myTurn = False
            spellNbr = self.spellNbr
            pm = self.pmNbr
            meLoc, mobsLocs = [], []

            self.waitTurn()
            myTurn = True

            if self.stopSignal.is_set():
                return
            meLoc = getPatternsLocs(meR, ME_Ps, meLoc)
            mobsLocs = getPatternsLocs(MAP_R, MOB_Ps, mobsLocs)

            if mobsLocs == [] or meLoc == []:
                nbrEchec += 1
                if (nbrEchec > 3):
                    resigne()
                    self.isDead.set()
                    PA_R.stopObserver()
                    return
            else:
                nbrEchec = 0
                try:
                    logger.debug('playing turn')
                    tL, tC, mtD = select(mobsLocs, meLoc[0])
                    logger.debug('mtD = ' + str(mtD))
                    while not self.stopSignal.is_set() and spellNbr > 0:
                        paChanged.clear()
                        if mtD < self.spellRange:
                            if mtD > 2:
                                useSpell("d", tL)
                            else:
                                useSpell("e", tL)
                            if paChanged.is_set():
                                spellNbr -= 1
                                wait(.8)
                                if tL.getColor() != tC:
                                    tL, tC, mtD = select(mobsLocs, meLoc[0])
                            else:
                                logger.debug('can t hit target, moving...')
                                meLoc, mtD, pm = move(meLoc[0], tL, min(pm, mtD - 1))
                        else:
                            logger.debug('target not in range')
                            meLoc, mtD, pm = move(meLoc[0], tL, pm)


                except:
                    pass
            if END_R.exists(END_COMBAT_P, 1):
                END_R.click(END_COMBAT_P)
                PA_R.stopObserver()
                if not myTurn: self.isDead.set()
                return
            else:
                meR = getNearBy(meLoc[0], 5 * u, 5 * v)
                type("f")


class Farmer(threading.Thread):
    def __init__(self, resource_pattern, src_path, fighter_thread, nbr_cycles=1, start_step=0, max_pods=18000, min_pods=2000):
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
        self.farm_path = self.loadFarmPath()
        self.curr_pods = min_pods

    def run(self):
        self.fighter_thread.start()
        path_length = len(self.farm_path)
        cycle = 0
        pods = 0
        while not self.stop_signal.is_set() and cycle < self.nbr_cycles:

            while not self.stop_signal.is_set() and self.currentStep < path_length:

                if self.fighter_thread.combatDetected.is_set():
                    pods += 150
                    logger.debug('waiting for fighter to end...')
                    self.fighter_thread.combatEnded.wait()
                    self.fighter_thread.combatEnded.clear()
                    if self.fighter_thread.isDead.is_set():
                        self.fighter_thread.isDead.clear()
                        break

                logger.debug('step number ' + str(self.currentStep) + ' ...')
                rtype, rregion = self.farm_path[self.curr_step]
                self.currentStep += 1

                if rtype != 'mapChange':
                    self.collectResource()

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
                    usePotion()
                sleep(2)
                logger.debug('cycle number' + str(cycle) + 'ended')

        self.fighter_thread.interrupt()
        logger.debug('farmer stopped')

    def collectResource(self, rtype, rregion):
        rpattern = self.resource_pattern[rtype]
        match = rregion.findBest(rpattern)
        if match:
            rregion.hover()
            sleep(0.3)
            current = Pattern(capture(rregion))
            rregion.click()
            with rregion:
                waitForChange(rregion)
                waitVanish(current.similar(0.6))
            return True
        return False

    def loadFarmPath(self):
        with open(self.src_path) as file:
            result = []
            for line in file:
                if line:
                    if line.startswith("#"):
                        continue
                    data_list = line.split(',')
                    rtype = data_list[0]
                    rec = [int(e.strip('\n')) for e in data_list[1:]]
                    resource_region = Region(*rec)
                    result.append((resource_region, rtype))
        return result

    def interrupt(self):
        self.stop_signal.set()


def cleanUp():
    fighter_thread.interrupt()
    # farmer.interrupt()


if __name__ == "__main__":
    atexit.register(cleanUp)
    farming_path = "bot.sikuli\\paths\\tanielaTrajet.txt"
    farm_path = os.path.join(src_dir, farming_path)

    Settings.MoveMouseDelay = 0.3
    Settings.ClickDelay = 0.1
    Settings.observeScanRate = 3
    fighter_thread = Fighter(READY_R, READY_P, pmNbr=4, spellNbr=2, spellRange=13, scanRate=3)
    # farmer  = Farmer(SMALL_RIVER_FISH_P, farm_path, fighter, startStep =0, nbrCycle = 5)
    # farmer.start()
    # farmer.join()
    fighter.start()
    fighter.join()
    # Fighter(READY_R,READY_P,3).start()
