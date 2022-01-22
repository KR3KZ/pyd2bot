from asyncio import protocols
from .mapPoint import MapPoint


class PathElement:
    _oStep:MapPoint
    _nOrientation:int

    def __init__(self, mp:MapPoint, i:int): 
        if mp is None:
            self._oStep = MapPoint()
        else:
            self._oStep = mp
        self._nOrientation = i
    
    @property
    def orientation(self) -> int: 
        return self._nOrientation
    
    @property
    def step(self) -> MapPoint: 
        return self._oStep
    
    @property
    def cellId(self) -> int:
        return self._oStep.cellId 

    def __str__(self) -> str:
        return "[PathElement(cellId:" + self.cellId + ", x:" + self._oStep.x + ", y:" + self._oStep.y + ", orientation:" + self._nOrientation + ")]"
    