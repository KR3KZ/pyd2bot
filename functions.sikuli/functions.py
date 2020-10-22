from sikuli.Sikuli import *
from constants import *
import traceback


def loadFarmingPath(src_path):
    with open(src_path) as file:
        farmSteps = []
        for line in file:
            pixelType, x, y = line.split(',')
            trgt = Location(int(x), int(y))
            farmSteps.append([trgt, pixelType])
    return farmSteps


def dist(aLoc, bLoc):
    return ((aLoc.getX() - bLoc.getX()) ** 2 + (aLoc.getY() - bLoc.getY()) ** 2) ** 0.5


def selectTarget(mobsLocs, meLoc):
    if (mobsLocs != []):
        DistsFromTargets = map(lambda l: dist(l, meLoc), mobsLocs)
        targetIndex = DistsFromTargets.index(min(DistsFromTargets))
        return targetIndex
    return None


def getMobsLocs():
    for p in MOB_Ps:
        try:
            mobsPatterns = MAP_R.findAll(p)
            mobsPositions = map(lambda m: m.getTarget(), mobsPatterns)
            return mobsPositions
        except FindFailed:
            pass
    return None


def getMeLoc():
    for p in ME_Ps:
        try:
            me = MAP_R.find(p)
            return me.getTarget()
        except:
            pass
    return None


def squareDistance(aLoc, bLoc):
    i = round(abs(aLoc.x - bLoc.x) / u)
    j = round(abs(aLoc.y - bLoc.y) / v)
    return int(max(i, j))


def getMoveSquares(meLoc, pms):
    V = []
    for i in range(-pms, pms + 1):
        for j in range(-pms, pms + 1):
            if (max(abs(i), abs(j)) <= pms and (i + j) % 2 == 0):
                V.append(Location(meLoc.x + i * u, meLoc.y + j * v))
    return V


def moveTowardsTarget(meLoc, targetLoc, pmNbr):
    if (pmNbr == 0): return None
    moveSquares = getMoveSquares(meLoc, pmNbr)
    DistsFromTargets = map(lambda sL: dist(targetLoc, sL), moveSquares)
    sDFT = sorted(DistsFromTargets)
    while (sDFT != []):
        nearestSquareIndex = DistsFromTargets.index(sDFT.pop(0))
        square = moveSquares[nearestSquareIndex]
        if (square.getColor() == EMPTY_SQUARE_COLOR):
            square.click()
            return square
    return None


def getNearBy(loc, w, h):
    return Region(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


def useSpell(shortCut, target):
    type(shortCut)
    wait(0.1)
    target.click()


def usePotion():
    FIRST_ITEM_R.click()
    USE_ITEM_R.click()


def eatBred():
    BRED_R.click()
    USE_MULT_R.click()
    USE_MULTI_MAX_R.click()
    USE_MULT_CONFIRM_R.click()


def resign():
    RESIGNE_R.click()
    RESIGNE_CONFIRM_R.click()


def waitForChange(region):
    with region:
        onChange(100)
        observe(10)
        stopObserver()
