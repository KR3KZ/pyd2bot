from functools import lru_cache
import json
import os
import os
from typing import Any

ROOTDIR = os.path.dirname(__file__)

class MapPosition:
    id:int
    posX:int
    posY:int
    outdoor:bool
    capabilities:int
    nameId:int  
    showNameOnFingerpost:bool   
    playlists:list[list[int]]
    subAreaId:int
    worldMap:int
    hasPriorityOnWorldmap:bool
    allowPrism:bool
    isTransition:bool
    mapHasTemplate:bool
    tacticalModeTemplateId:int
    hasPublicPaddock:bool
    
    with open(os.path.join(ROOTDIR, "MapPositions.json")) as fp:
        _json = json.load(fp)
        _positions = {}
        for mpos in _json:
            _positions[int(mpos["id"])] = mpos
        del _json
        
    def __init__(self, dictionary:dict[str, Any]):
        for k, v in dictionary.items():
            setattr(self, k, v)
            
    @staticmethod
    @lru_cache(maxsize = 100)
    def getMapPositionById(mapId) -> 'MapPosition':
        if mapId not in MapPosition._positions:
            return None
        return MapPosition(MapPosition._positions[mapId])
