from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MoodSmileyUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    smileyId:int
    
    
    def __post_init__(self):
        super().__init__()
    