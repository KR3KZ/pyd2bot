from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class StatedElement(NetworkMessage):
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    
    
    def __post_init__(self):
        super().__init__()
    