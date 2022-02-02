from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class TeleportToBuddyAnswerMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    accept:bool
    
    
    def __post_init__(self):
        super().__init__()
    