from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.utils.pathFinding import Pathfinding



    

currMapID = 193331717

currCellId = 130
targetCellId = 63
pf = Pathfinding()

currMap = MapLoader.load(193331717)

if not currMap.cells[103].isAccessibleDuringRP():
    raise Exception("impossible !!!")

pf.updatePosition(currMap, currCellId)

keyMouvements = pf.getCellsPathTo(targetCellId)
print(keyMouvements)