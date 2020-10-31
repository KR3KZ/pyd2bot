import threading
import traceback
from core.grid import Grid
from time import sleep
from .taf import *
import core.env as env

log = Log()
lock = threading.Lock()


class Fighter(threading.Thread):
    def __init__(self, nbr_pm, spell, scan_rate=3):
        threading.Thread.__init__(self, name='Farmer')
        self.scan_rate = scan_rate
        self.spell = spell
        self.nbr_pm = nbr_pm
        self.died = threading.Event()
        self.stopSignal = threading.Event()
        self.combatDetected = threading.Event()
        self.combatEnded = threading.Event()
        self.combat_ended_observer = AppearObserver(env.COMBAT_ENDED_POPUP_R, env.COMBAT_ENDED_POPUP_P,
                                                    self.onCombatEnded)

    def run(self):
        log.info('fighter running')
        while not self.stopSignal.is_set():
            self.waitCombatStarted()
            with lock:
                try:
                    self.combatAlgo()
                except Exception as e:
                    log.info(traceback.print_exc())
                    self.interrupt()
                self.combatDetected.clear()
                log.info('combat ended')
        log.info('fighter stopped')

    def waitCombatStarted(self):
        r = env.READY_R.waitAppear(env.FOREVER)
        if r:
            wait(0.5)
            env.READY_R.click()
            self.combatDetected.set()
            log.info('Combat started')

    def interrupt(self):
        env.READY_R.stopWait.set()
        self.combat_ended_observer.stop()
        self.combat_ended_observer.join()
        self.combatEnded.set()
        self.stopSignal.set()

    def waitTurn(self):
        while not self.stopSignal.is_set() and not self.combatEnded.is_set():
            if env.MY_TURN_CHECK_R.getTarget().getColor() == env.Color.MY_TURN_COLOR:
                log.info('Bot turn started')
                break
            wait(0.33)

    def useSpell(self, target):
        pa_observer = ChangeObserver(env.PA_R)
        pa_observer.start()
        type(self.spell['shortcut'])
        target.click()
        res = pa_observer.changed.waitAppear(3)
        pa_observer.join()
        return res

    def combatAlgo(self):
        log.info('combat started')
        self.combatEnded.clear()
        self.combat_ended_observer.start()

        # main combat loop
        while not self.combatEnded.wait(1):
            self.waitTurn()

            # Parse combat grid
            grid = Grid(env.COMBAT_R, env.VCELLS, env.HCELLS)

            # select nearest target to hit
            target = self.selectTarget(mobs, bot)
            spell_nbr = self.spell['nbr']
            pm = self.nbr_pm

            # in turn loop
            while not self.stopSignal.is_set() and spell_nbr > 0:
                log.info('My distance from target = ' + str(target['dist']))
                log.info("pm: ", pm, ", nbr spell: ", spell_nbr)

                # if target is in spell range
                if target['dist'] <= self.spell['range']:
                    log.info("target is in spell range")
                    target['in-range'] = True

                    # if nbr casts allowed reached try to switch target
                    if target['nbr-casted-on'] == self.spell['nbr-on-same']:
                        if len(mobs) > 1:
                            other_mobs = [m for m in mobs if m != target['match']]
                            target = self.selectTarget(other_mobs, bot)
                        else:
                            # cant recast the spell on target and no other targets
                            break

                    # if spell hits the target
                    if self.useSpell(target['pos']):
                        log.info("I touched the target")
                        spell_nbr -= 1
                        target['nbr-casted-on'] += 1
                        # if target dies after spell cast
                        if not target['region'].waitAppear(target['snippet'], 3):
                            log.info("target died")
                            if len(mobs) == 1:
                                self.combatEnded.wait(5)
                                return
                            else:
                                mobs.pop(target['idx'])
                                target = self.selectTarget(mobs, bot)
                        continue

                log.info("I can't hit the target")
                # if target not reachable and bot has not pms skip turn
                if pm == 0:
                    break

                if self.stopSignal.is_set():
                    return
                if target['in-range']:
                    search_range = pm
                else:
                    search_range = min(pm, target['dist'] - self.spell['range'])

                cell_pos = getNearestCell(bot_pos, target['pos'], search_range)

                if cell_pos:
                    pm_to_cell = squareDist(cell_pos, bot_pos)
                    log.info("moving {} to new nearest cell".format(pm_to_cell))
                    cell_pos.click()
                    pm = pm - pm_to_cell
                    bot_pos = cell_pos
                    target['dist'] = squareDist(target['pos'], bot_pos)

            # skip turn
            env.OUT_OF_COMBAT_R.hover()
            log.info("bot skipped his turn")
            type(Key.SPACE)
            wait(0.5)
