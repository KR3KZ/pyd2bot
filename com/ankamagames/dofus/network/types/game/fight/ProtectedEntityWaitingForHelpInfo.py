from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ProtectedEntityWaitingForHelpInfo(NetworkMessage):
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    
    
    def __post_init__(self):
        super().__init__()
    