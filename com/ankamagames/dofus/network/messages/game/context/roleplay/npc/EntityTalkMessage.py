from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class EntityTalkMessage(NetworkMessage):
    entityId:int
    textId:int
    parameters:list[str]
    
    
    def __post_init__(self):
        super().__init__()
    