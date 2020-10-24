from sikuli.Sikuli import *
import constants as cnst


def dist(pos1, pos2):
    return ((pos1.getX() - pos2.getX()) ** 2 + (pos1.getY() - pos2.getY()) ** 2) ** 0.5


def selectTarget(mobs_pos, me_pos):
    if mobs_pos:
        tI = min(range(len(mobs_pos)), key=lambda x: squareDist(mobs_pos[x], me_pos))
        tgt_loc = mobs_pos.pop(tI)
        return tgt_loc
    return None


def squareDist(pos1, pos2):
    i = round(abs(pos1.x - pos2.x) / cnst.CELL_W)
    j = round(abs(pos1.y - pos2.y) / cnst.CELL_H)
    return int(max(i, j))


def getMoveSquares(loc, pm):
    V = []
    if pm != 0:
        from itertools import product
        for i, j in product(range(-pm, pm + 1), range(-pm, pm + 1)):
            if i * j != 0 and (i + j) % 2 == 0 and max(abs(i), abs(j)) <= pm:
                square_pos = Location(loc.x + i * cnst.CELL_W, loc.y + j * cnst.CELL_H)
                if square_pos.getColor() == cnst.EMPTY_SQUARE_COLOR:
                    V.append(square_pos)
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
    wait(0.3)
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
    snippet = capture(cnst.MINIMAP_R)
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