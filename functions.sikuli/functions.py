from sikuli.Sikuli import *
import constants as cnst


def loadFarmingPath(src_path):
    with open(src_path) as file:
        farmSteps = []
        for line in file:
            pixelType, x, y = line.split(',')
            trgt = Location(int(x), int(y))
            farmSteps.append([trgt, pixelType])
    return farmSteps


def dist(pos1, pos2):
    return ((pos1.getX() - pos2.getX()) ** 2 + (pos1.getY() - pos2.getY()) ** 2) ** 0.5


def selectTarget(mobs_pos, me_pos):
    if mobs_pos:
        DistsFromTargets = map(lambda l: dist(l, me_pos), mobs_pos)
        targetIndex = DistsFromTargets.index(min(DistsFromTargets))
        return targetIndex
    return None


def getMobsLocs():
    for p in cst.MOB_Ps:
        try:
            mobsPatterns = cst.MAP_R.findAll(p)
            mobsPositions = map(lambda m: m.getTarget(), mobsPatterns)
            return mobsPositions
        except FindFailed:
            pass
    return None


def getMeLoc():
    for p in cnst.ME_Ps:
        try:
            me = cst.MAP_R.find(p)
            return me.getTarget()
        except:
            pass
    return None


def squareDistance(pos1, pos2):
    i = round(abs(pos1.x - pos2.x) / cnst.CELL_W)
    j = round(abs(pos1.y - pos2.y) / cnst.CELL_H)
    return int(max(i, j))


def getMoveSquares(meLoc, pms):
    V = []
    for i in range(-pms, pms + 1):
        for j in range(-pms, pms + 1):
            if max(abs(i), abs(j)) <= pms and (i + j) % 2 == 0:
                V.append(Location(meLoc.x + i * cnst.CELL_W, meLoc.y + j * cnst.CELL_H))
    return V


def moveTowardsTarget(me_pos, tgt_pos, pm_nbr):
    if pm_nbr == 0:
        return None
    move_squares = getMoveSquares(me_pos, pm_nbr)
    dists_from_targets = list(map(lambda l: dist(tgt_pos, l), move_squares))
    tgts_dist = sorted(dists_from_targets)
    while tgts_dist:
        nearest_square_index = dists_from_targets.index(tgts_dist.pop(0))
        square = move_squares[nearest_square_index]
        if square.getColor() == EMPTY_SQUARE_COLOR:
            square.click()
            return square
    return None


def getNearBy(loc, w, h):
    return Region(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


def useSpell(shortcut, target):
    type(shortcut)
    wait(0.1)
    target.click()


def usePotion():
    cnst.FIRST_ITEM_R.click()
    cnst.USE_ITEM_R.click()


def eatBred():
    cnst.BRED_R.click()
    cnst.USE_MULT_R.click()
    cnst.USE_MULTI_MAX_R.click()
    cnst.USE_MULT_CONFIRM_R.click()


def resign():
    cnst.RESIGN_R.click()
    cnst.RESIGN_CONFIRM_R.click()


def waitForChange(region):
    with region:
        onChange(100)
        observe(10)
        stopObserver()


def changeMap(tgt):
    snippet = capture(MAP_INFO_R)
    tgt.click()
    while MAP_INFO_R.exists(Pattern(snippet).similar(0.85)):
        wait(0.5)


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
