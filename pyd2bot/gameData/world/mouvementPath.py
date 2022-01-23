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

    def __init__(self, pelist):
        super().__init__(pelist)
        self.end = MapPoint()
        self.start = MapPoint()
    
    def compress(self) -> None: 
        size = len(self)
        ret = [self[0]]
        if size > 0: 
            for i in range(1, size - 1):
                if self[i].orientation != self[i + 1].orientation:
                    ret.append(self[i])
        ret.append(self[-1])
        super().__init__(ret)
        
    def fill(self): 
        if len(self) > 0:
            pe = PathElement(self.end, 0)
            print("end : " + str(self.end))
            self.append(pe)
            vectorSize = len(self)
            print("vectorSize: " + str(vectorSize))
            print("self: " + str(self))
            for i in range(vectorSize - 1):
                if i > self.MAX_PATH_LENGTH:
                    raise Exception("Path too long. Maybe an orientation problem ?")
                pe = self[i]
                if abs(pe.step.x - self[i + 1].step.x) > 1 or abs(pe.step.y - self[i + 1].step.y) > 1:
                    pe2 = PathElement(None, pe.orientation) 
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
            del self[-1]

    def getCells(self) -> list[int]: 
        size = len(self)
        cells = size * [_.step.cellID for _ in self] + [self.end.cellID]
        return cells
    
    def replaceEnd(self, mp:MapPoint) -> None: 
        self.end = mp
    
    def getServerMovement(self) -> list[int]: 
        self.compress()
        result = []
        for pe in self:
            nb = (pe.orientation << 12) + (pe.step.cellID & 4095)
            result.append(nb)
        return result
    
    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
    
