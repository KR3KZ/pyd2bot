import math
from pyd2bot.gameData.world.map import Map
from pyd2bot.gameData.world.mapPoint import MapPoint
from pyd2bot.utils.mapTools import MapTools


class LosDetector:
    
    def __init__():
        pass
    
    def getCell(self, mapData:Map, spellrange:list[int], refPosition:MapPoint) -> list[int]: 
        orderedCell:list = list()
        for i in range(spellrange):
            mp = MapPoint.fromCellId(range[i])
            orderedCell.append({
                "p":mp,
                "dist":refPosition.distanceToCell(mp)
            })
        sorted(orderedCell, key=lambda x:x["dist"], reverse=True)
        tested = dict[str, bool]()
        result:list[int] = list[int]()
        for i in range(len(orderedCell)):
            
            p = MapPoint(orderedCell[i].p)
            if not (tested.get(f"{p.x}_{p.y}") is not None and refPosition.x + refPosition.y != p.x + p.y and refPosition.x - refPosition.y != p.x - p.y):
            
                line = MapTools.getCellsCoordBetween(refPosition.cellId, p.cellId)
                if len(line) == 0:
                    result.append(p.cellId)
                
                else:
                    los = True
                    for j in range(len(line)):
                    
                        currentPoint = str(math.floor(line[j].x)) + "_" + str(math.floor(line[j].y))
                        if MapPoint.isInMap(line[j].x, line[j].y):

                            if j > 0 and mapData.hasEntity(math.floor(line[j - 1].x), math.floor(line[j - 1].y), True):
                                los = False
                            
                            elif line[j].x + line[j].y == refPosition.x + refPosition.y or line[j].x - line[j].y == refPosition.x - refPosition.y:
                                los = los and mapData.pointLos(math.floor(line[j].x), math.floor(line[j].y), True)
                            
                            elif tested.get(currentPoint) is None:
                                los = los and mapData.pointLos(math.floor(line[j].x), math.floor(line[j].y), True)
                            
                            else:
                                los = los and tested[currentPoint]
                        
                    tested[currentPoint] = los
                
        
        for i in range(spellrange):
            mp = MapPoint.fromCellId(range[i])
            if tested[mp.x + "_" + mp.y]:
                result.append(mp.cellId)
        
        return result
    
