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
    
    def compress(self) -> None: 
        size = len(self)
        ret = [self[0]]
        if size > 0: 
            for i in range(1, size - 1):
                if self[i]._nOrientation != self[i - 1]._nOrientation:
                    ret.append(self[i])
        ret.append(self[-1])
        super().__init__(ret)

    def getCells(self) -> list[int]: 
        cells = [_.step.cellID for _ in self]
        return cells
    
    def getServerMovement(self) -> list[int]: 
        self.compress()
        result = []
        for pe in self:
            nb = (pe._nOrientation << 12) + (pe.step.cellID & 4095)
            result.append(nb)
        return result
    
    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
    
