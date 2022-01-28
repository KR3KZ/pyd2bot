from asyncio.log import logger
import logging
from time import perf_counter
from pyd2bot.gameData.mapReader import MapLoader
from com.ankamagames.atouin.data.map.map import CellData, Map
from com.ankamagames.jerakine.types.positions.mapPoint import MapPoint
from pyd2bot.utils.pathFinding import Pathfinding
from pyd2bot.gameData.world.mapZones import MapZones


with open("pyd2bot.log", "w") as f:
    f.flush()


def getCellAfterMapChange(srcId:int, direction:int) -> int:
    """Detemine the cell after a map changement.
    """
    if direction == Map.RIGHT:
        return srcId - (Map.WIDTH - 1)

    elif direction == Map.LEFT:
        return srcId + (Map.WIDTH - 1)

    elif direction == Map.UP:
        return (srcId - Map.WIDTH * 2) + 560

    elif direction == Map.DOWN:
        return (srcId + Map.WIDTH * 2) - 560
        
    raise Exception("Invalid direction for changing map.")

if __name__ == '__main__':
    sourceMapId = 190054912
    startCellId = 132
    targetMapId = 189792257
    srcMap = MapLoader.load(sourceMapId)
    mz = MapZones(srcMap).getZone(startCellId)
    srcMap.printGrid()
        # print(srcMap.cells[i].id // 2 * Map.WIDTH, end=", ")

    # print(len(mz), len(mz[0]))
    # srcCellId = None
    # r = getCellAfterMapChange(531, Map.RIGHT)
    # print(r)

    pf = Pathfinding()
    # srcMap = MapLoader.load(sourceMapId)
    # p = pf.toMap(sourceMapId, targetMapId, startCellId)
    # print(p)
