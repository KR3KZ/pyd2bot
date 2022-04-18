from time import perf_counter
from types import FunctionType
from com.ankamagames.dofus.modules.utils.pathFinding.world.WorldPathFinder import (
    WorldPathFinder,
)
from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import (
    EnterFrameDispatcher,
)


def findPath(
    wpf: WorldPathFinder,
    currCellId,
    currMap,
    destinationMapId: float,
    callback: FunctionType,
) -> None:
    if not wpf.isInitialized():
        print("not initiéalized")
        callback(None)
        return
    playerCell = currMap.cells[currCellId]
    wpf.src = wpf.worldGraph.getVertex(currMap.id, playerCell.linkedZoneRP)
    if wpf.src is None:
        callback(None)
        return
    wpf.linkedZone = 1
    WorldPathFinder.callback = callback
    wpf.dst = destinationMapId
    wpf.next()


def onPathFound(a, path) -> None:
    if path is None:
        print("path is None")
    else:
        print("path found")
        for e in path:
            print(e)


if __name__ == "__main__":
    currMapID = 155975689
    dstMapID = 193331717
    playedEntityCellId = 36
    targetCellId = 221
    dataMap = MapLoader().load(currMapID)
    playerCell = dataMap.cells[playedEntityCellId]
    wpf = WorldPathFinder()
    wpf.init()
    r = findPath(wpf, playedEntityCellId, dataMap, dstMapID, onPathFound)

    # cell :171 -> Vertex(mapId=155975689.0, zoneId=1, uid=1935)
