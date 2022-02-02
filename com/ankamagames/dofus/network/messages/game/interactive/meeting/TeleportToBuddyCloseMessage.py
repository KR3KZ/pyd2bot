from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportToBuddyCloseMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    
    
    def __post_init__(self):
        super().__init__()
    