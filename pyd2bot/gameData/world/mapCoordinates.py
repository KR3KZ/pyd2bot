

import os
import json
from typing import Any
from pyd2bot.gameData.world.mapPosition import MapPosition

ROOTDIR = os.path.dirname(__file__)


class MapCoordinates:
    MODULE = "MapCoordinates"
    UNDEFINED_COORD = -2147483648
    compressedCoords:int
    mapIds:list[int]
    _x = -2147483648
    _y = -2147483648
    _maps:list[MapPosition]
    
    with open(os.path.join(ROOTDIR, "MapCoordinates.json")) as fp:
        _json = json.load(fp)
    _coords = {}
    for mcoord in _json:
        _coords[int(mcoord["compressedCoords"])] = mcoord
    
    def __init__(self, dictionary:dict[str, Any]):
        for k, v in dictionary.items():
            setattr(self, k, v)
            
    def getMapCoordinatesByCompressedCoords(self, i:int) -> 'MapCoordinates': 
        return MapCoordinates(MapCoordinates._coords[i])
    
    def getMapCoordinatesByCoords(self, i1:int, i2:int) -> 'MapCoordinates': 
        return MapCoordinates.getMapCoordinatesByCompressedCoords((MapCoordinates.getCompressedValue(i1) << 16) + MapCoordinates.getCompressedValue(i2))
    
    @staticmethod
    def getSignedValue(i:int) -> int: 
        i2 = i & 32767
        return -i2 if (i & 0x8000) > 0 else i2
    
    @staticmethod
    def getCompressedValue(i:int) -> int: 
        return (0x8000 | (i & 32767)) if i < 0 else i & 32767
    
    @property
    def x(self) -> int: 
        if self._x == self.UNDEFINED_COORD:
            self._x = self.getSignedValue((self.compressedCoords & 0xFFFF0000) >> 16)
        return self._x
    
    @property
    def y(self) -> int: 
        if self._y == self.UNDEFINED_COORD:
            self._y = self.getSignedValue(self.compressedCoords & 0xFFFF)
        return self._y
    
    def getMaps(self, ) -> list[MapPosition]: 
        if self._maps == None: 
            self._maps = list[MapPosition]()
            for mapId in self.mapIds:
                self._maps.append(MapPosition.getMapPositionById(mapId))
        return self._maps
    
