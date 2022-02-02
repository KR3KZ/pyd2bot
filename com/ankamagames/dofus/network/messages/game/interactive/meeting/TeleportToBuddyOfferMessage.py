from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportToBuddyOfferMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    timeLeft:int
    
    
    def __post_init__(self):
        super().__init__()
    