from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportBuddiesRequestedMessage(NetworkMessage):
    dungeonId:int
    inviterId:int
    invalidBuddiesIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    