from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class DisplayNumericalValuePaddockMessage(NetworkMessage):
    rideId:int
    value:int
    type:int
    
    
    def __post_init__(self):
        super().__init__()
    