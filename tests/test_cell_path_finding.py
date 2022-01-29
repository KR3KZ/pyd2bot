from time import perf_counter
from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader
from pyd2bot.utils.pathFinding import Pathfinding
    

if __name__ == '__main__':
    currMapID = 188746756
    currCellId = 470
    targetCellId = 221

    pf = Pathfinding()
    currMap = MapLoader.load(currMapID)

    pf.updatePosition(currMap, currCellId)
    s = perf_counter()
    keyMouvements = pf.getCellsPathTo(targetCellId)
    end = perf_counter() - s
    print("path duration estimated: " + str(pf.getCellsPathDuration()))
    print("exec time: " + str(end))
    print(keyMouvements)
