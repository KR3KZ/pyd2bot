from .mapPoint import MapPoint
from .pathElement import PathElement


class MovementPath(list[PathElement]):
    RIGHT = 0
    DOWN_RIGHT = 1
    DOWN = 2
    DOWN_LEFT = 3
    LEFT = 4
    UP_LEFT = 5
    UP = 6
    UP_RIGHT = 7
    MAX_PATH_LENGTH = 100

    def __init__(self):
        super().__init__()
        self._oEnd = MapPoint()
        self._oStart = MapPoint()
    
    @property
    def start(self) -> MapPoint: 
        return self._oStart
    
    @property
    def end(self) -> MapPoint: 
        return self._oEnd
    
    def compress(self) -> None: 
        size = len(self)
        if size > 0: 
            for i in range(1, size - 1):
                if self[i].orientation == self[i + 1].orientation:
                    del self[i]
        
    def fill(self): 
        if self > 0:
            pe = PathElement(None, 0)
            pe.orientation = 0
            pe.step = self._oEnd
            self.append(pe)
            vectorSize = len(self)
            for i in range(vectorSize):
                if i > self.MAX_PATH_LENGTH:
                    raise Exception("Path too long. Maybe an orientation problem ?")
                pe = self[i]
                if abs(pe.step.x - self[i + 1].step.x) > 1 or abs(pe.step.y - self[i + 1].step.y) > 1:
                    pe2 = PathElement(None, 0)
                    pe2.orientation = pe.orientation
                    if pe2.orientation == self.RIGHT: 
                        pe2.step = MapPoint.fromCoords(pe.step.x + 1, pe.step.y + 1)
                    elif pe2.orientation == self.DOWN_RIGHT:
                        pe2.step = MapPoint.fromCoords(pe.step.x + 1, pe.step.y)
                    elif pe2.orientation == self.DOWN:
                        pe2.step = MapPoint.fromCoords(pe.step.x, pe.step.y + 1)
                    elif pe2.orientation == self.DOWN_LEFT:
                        pe2.step = MapPoint.fromCoords(pe.step.x - 1, pe.step.y)
                    elif pe2.orientation == self.LEFT:
                        pe2.step = MapPoint.fromCoords(pe.step.x - 1, pe.step.y + 1)
                    elif pe2.orientation == self.UP_LEFT:
                        pe2.step = MapPoint.fromCoords(pe.step.x - 1, pe.step.y)
                    elif pe2.orientation == self.UP:
                        pe2.step = MapPoint.fromCoords(pe.step.x, pe.step.y - 1)
                    elif pe2.orientation == self.UP_RIGHT:
                        pe2.step = MapPoint.fromCoords(pe.step.x + 1, pe.step.y)
                    self[i + 1] = pe2
            del self[- 1]

    def getCells(self) -> list[int]: 
        size = len(self)
        cells = size * [_.step.cellID for _ in self] + [self._oEnd.cellID]
        return cells
    
    def replaceEnd(self, mp:MapPoint) -> None: 
        self._oEnd = mp
    
    def getServerMovement(self) -> list[int]: 
        self.compress()
        result = list[int]
        mpLength = len(self)
        
        if self[mpLength - 1] != None:
            result = (mpLength + 1) * [0]
        else:
            result = mpLength * [0]
            
        for i in range(mpLength):
            pe = self[i]
            nb = ((pe.orientation & 7) << 12) | (pe.step.cellID & 4095)
            result[i] = nb
        
        if pe: 
            nb = ((pe.orientation & 7) << 12) | (self.end.cellID & 4095)
            result[mpLength] = nb
        
        return result
    
