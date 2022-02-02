from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GuildHouseRemoveMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    
    
    def __post_init__(self):
        super().__init__()
    