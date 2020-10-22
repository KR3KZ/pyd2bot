from sikuli.Sikuli import *
import constants as cnst


def dist(pos1, pos2):
    return ((pos1.getX() - pos2.getX()) ** 2 + (pos1.getY() - pos2.getY()) ** 2) ** 0.5


def selectTarget(mobs_pos, me_pos):
    if mobs_pos:
        dists_from_targets = map(lambda l: dist(l, me_pos), mobs_pos)
        target_index = dists_from_targets.index(min(dists_from_targets))
        return target_index
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
        if square.getColor() == cnst.EMPTY_SQUARE_COLOR:
            square.click()
            return square
    return None


def getNearBy(loc, w, h):
    return Region(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


def useSpell(shortcut, target):
    type(shortcut)
    wait(0.1)
    target.click()


def useRappelPotion():
    type(cnst.RAPPEL_POTION_SHORTCUT)


def waitForChange(region):
    with region:
        onChange(100)
        observe(10)
        stopObserver()


def changeMap(tgt):
    time = 0
    snippet = capture(cnst.MAP_INFO_R)
    while time < cnst.CHANGE_MAP_TIMEOUT:
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
