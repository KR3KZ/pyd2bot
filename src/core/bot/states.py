from enum import Enum

class PosRequestState(Enum):
    idle = 0
    msgSent = 1
    gotResponse = 2
    
class MapChangeState(Enum):
    idle = 0
    clicked = 1
    moving = 4
    requested = 2
    done = 3

class FarmingState(Enum):
    idle = 0
    clicked = 1
    moving = 2
    requested = 3
    startedCollect = 4
    endedCollect = 5
    