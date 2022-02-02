from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayDelayedActionMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    
    
    def __post_init__(self):
        super().__init__()
    