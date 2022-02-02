from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameActionMarkedCell(NetworkMessage):
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    
    
    def __post_init__(self):
        super().__init__()
    