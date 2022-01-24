from pyd2bot.gameData.mapReader import MapLoader
from pyd2bot.utils.pathFinding import Pathfinding
    

currMapID = 188746756
currCellId = 470
targetCellId = 221

pf = Pathfinding()
currMap = MapLoader.load(currMapID)


pf.updatePosition(currMap, currCellId)
keyMouvements = pf.getCellsPathTo(targetCellId)
print(keyMouvements)
# [25046, 29114, 24991, 29059, 24950, 29018, 24908, 28976, 24867, 28907, 28893]
# [25046, 29114, 24924, 20716, 20701]