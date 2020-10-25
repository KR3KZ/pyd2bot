from sikuli.Sikuli import *
import java.awt.Color as Color
import threading
import atexit
from math import sqrt, floor, ceil

class CellFindError(Exception):
    pass

# Regions
MAP_R = Region(2,29,1918,1002)
MAP_INFO_R = Region(4,856,306,172)
COMBAT_R = Region(332,28,1257,1004)
PM_R = Region(793,993,27,34)
PA_R = Region(740,997,34,24)
END_COMBAT_R = Region(841,701,244,66)

READY_R = Region(1312,925,145,66)
YOUR_TURN_R = Region(1312,925,145,66)
END_COMBAT_CLOSE_R = Region(1231,721,22,18)

MY_TURN_CHECK_LOC = Location(1431, 965)
MY_TURN_COLOR = Color(123,143,0)

# Patterns

READY_P = Pattern("1603357824947.png")
END_COMBAT_P = "END_COMBAT_P.png"
YOUR_TURN_P = "YOUR_TURN_P.png"

END_COMBAT_CLOSE_P = "END_COMBAT_CLOSE_P.png"

ME_P = [Pattern("ME_P1.png").targetOffset(3,3), Pattern("ME_P2.png").targetOffset(-3,8), Pattern("1603394186463.png").targetOffset(2,2), Pattern("1603394202485.png").targetOffset(-2,-8), Pattern("1603403880774.png").similar(0.61).targetOffset(1,13), Pattern("1603408051708.png").targetOffset(5,7), Pattern("1603408090329.png").targetOffset(0,-6), Pattern("1603407845345.png").targetOffset(0,13)]
MOB_P = [Pattern("1603395992136.png").targetOffset(1,10), "1603396008837.png", "1603396021085.png", "1603396033757.png", "1603396047136.png", Pattern("1603396061137.png").similar(0.64), Pattern("1603396075836.png").targetOffset(-2,6),"1603396143388.png"]

# Vars
CELL_W = 42
CELL_H = 21
CHANGE_MAP_DELAY = 2
EMPTY_SQUARE_COLOR = Color(90, 125, 62)
DU = (-1, -1)
DL =(-1, 1)
DD = (1, 1)
DR = (1, -1)
# timers
CHANGE_MAP_TIMEOUT = 60

# shortcuts
RAPPEL_POTION_SHORTCUT = "e"
FARM_SPELL = {
        "shortcut": "z",
        "range": 6,
        "nbr": 3
}

def highlightPath(start_loc, path):
    x = start_loc.absx
    y = start_loc.absy
    for dx, dy in path:
        x = x + dx * CELL_W
        y = y + dy * CELL_H
        Region(x, y, 1, 1).highlight(0.2)
    return Location(x, y)


def getNearByRegion(loc, w, h):
    return Region(loc.absx - w / 2, loc.absy - h / 2, w, h)


def dist(pos1, pos2):
    return ((pos1.absx - pos2.absx) ** 2 + (pos1.absy - pos2.absy) ** 2) ** 0.5


def selectTarget(mobs_pos, me_pos):
    tI = min(range(len(mobs_pos)), key=lambda x: squareDist(mobs_pos[x], me_pos))
    tgt_loc = mobs_pos.pop(tI)
    return tgt_loc


def squareDist(pos1, pos2):
    i = round(abs(pos1.absx - pos2.absx) / CELL_W)
    j = round(abs(pos1.absy - pos2.absy) / CELL_H)
    return max(int(i), int(j))

def similarColor(c1, c2, th=0.7):
    rmean = ( c1.red + c2.red ) / 2
    r = c1.red - c2.red
    g = c1.green - c2.green
    b = c1.blue - c2.blue
    return sqrt((((512 + rmean)*r*r)>>8) + 4*g*g + (((767 - rmean)*b*b)>>8))

    
def getMoveSquares(loc, pm):
    V = []
    if pm != 0:
        from itertools import product
        for i, j in product(range(-pm, pm + 1), range(-pm, pm + 1)):
            if (i != 0 or j != 0) and (i + j) % 2 == 0 and max(abs(i), abs(j)) <= pm:
                square_pos = Location(loc.absx + i * CELL_W, loc.absy + j * CELL_H)
                if similarColor(square_pos.getColor(), EMPTY_SQUARE_COLOR) < 100:
                    # print(similarColor(square_pos.getColor(), EMPTY_SQUARE_COLOR))
                    V.append(square_pos)
    return V


def mobExists(mobs, mob):
    for m in mobs:
        if squareDist(m, mob) == 0:
            return True
    return False


def removeDuplicates(mobs_pos):
    res = []
    for mob in mobs_pos:
        if not mobExists(res, mob):
            res.append(mob)
    return res
        
def getNearestCell(me_pos, tgt_pos, pm_nbr):
    if pm_nbr == 0:
        return None
    move_squares = getMoveSquares(me_pos, pm_nbr)
    dists_from_targets = list(map(lambda l: dist(tgt_pos, l), move_squares))
    tgts_dist = sorted(dists_from_targets)
    while tgts_dist:
        nearest_square_index = dists_from_targets.index(tgts_dist.pop(0))
        cell_pos = move_squares[nearest_square_index]
        getNearByRegion(cell_pos, 1, 1).highlight(0.1)
        if similarColor(cell_pos.getColor(), EMPTY_SQUARE_COLOR) < 50:
            return cell_pos
    return None


def getNearBy(loc, w, h):
    return Region(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


def useSpell(shortcut, target):
    type(shortcut)
    wait(0.3)
    target.click()


def useRappelPotion():
    type(RAPPEL_POTION_SHORTCUT)


def waitForChange(region):
    with region:
        onChange(100)
        observe(10)
        stopObserver()


def changeMap(tgt):
    time = 0
    snippet = capture(MAP_INFO_R)
    while time < CHANGE_MAP_TIMEOUT:
        tgt.click()
        if waitVanish(Pattern(snippet).exact(), 10):
            break
        time += 10


def loadFarmPath(file_path):
    with open(file_path) as file:
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


def collectResource(rpattern, rregion):
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


def happened(event, signal, rep=False):
    signal.set()
    if rep:
        event.repeat()
        
def cleanUp():
    PA_R.stopObserver()


def waitTurn():
    print('waiting bot turn ...')
    while True:
        try:
            YOUR_TURN_R.wait(YOUR_TURN_P, 0.33)
            if MY_TURN_CHECK_LOC.getColor() == MY_TURN_COLOR:  
                break
        except FindFailed as e:
            pass

def waitCombatStarted():
    while True:
        try:
            READY_R.wait(READY_P, 0.33)
            break
        except FindFailed as e:
            pass
    
        
atexit.register(cleanUp)
paChanged = threading.Event()

waitCombatStarted()
READY_R.click()

while True:
    waitTurn()
    
    PA_R.onChange(lambda e: happened(e, paChanged, True))
    PA_R.observeInBackground(FOREVER)
    
    me_match = COMBAT_R.findBest(ME_P)
    me_pos = me_match.getTarget()
    Region(me_match).highlight(0.2)
    if not me_pos:
        raise
    
    spell_nbr = 2
    pm = 5
    
    mobs_match = COMBAT_R.findAny(MOB_P)
    mobs_pos = removeDuplicates([e.getTarget() for e in mobs_match])

    for m in mobs_pos:
        Region(m.absx, m.absy, 1, 1).highlight(0.5)
    
    # Get next target infos
    tgt_pos = selectTarget(mobs_pos, me_pos)
    tgt_color = tgt_pos.getColor()
    me_tgt_dist = squareDist(tgt_pos, me_pos)
    
    while spell_nbr > 0:
        print('My distance from target = ' + str(me_tgt_dist))
        print("pm: ", pm, ", nbr spell: ", spell_nbr)
        paChanged.clear()
        
        if me_tgt_dist <= FARM_SPELL['range']:
            print("target in range")
            
            for i in range(3):
                useSpell(FARM_SPELL['shortcut'], tgt_pos)
                wait(0.5)
                if paChanged.is_set():
                    break
                wait(0.3)
                
            if paChanged.is_set():
                spell_nbr -= 1
                print("I hitted the target")
                if tgt_pos.getColor() != tgt_color:
                    tgt_pos = selectTarget(mobs_pos, me_pos)
                continue
            
        print("I can't hit the target")
        if pm > 0:
            search_range = min(pm, me_tgt_dist - FARM_SPELL['range'])
            cell_pos = getNearestCell(me_pos, tgt_pos, search_range)
            if cell_pos:
                pm_to_cell = squareDist(cell_pos, me_pos)
                cell_pos.click()
                pm = pm - pm_to_cell 
                print("moved {} to new nearest cell".format(pm_to_cell))
                me_pos = cell_pos
                me_tgt_dist = squareDist(tgt_pos, me_pos)
            
        else:
            break
        
    PA_R.stopObserver()
    PA_R.hover()
    print("bot skip turn")
    type(Key.SPACE)
    wait(0.5)
