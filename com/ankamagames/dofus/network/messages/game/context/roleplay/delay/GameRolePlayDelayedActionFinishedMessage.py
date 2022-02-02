from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    
    
    def __post_init__(self):
        super().__init__()
    