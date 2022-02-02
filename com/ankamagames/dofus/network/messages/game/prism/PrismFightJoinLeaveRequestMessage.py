from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    subAreaId:int
    join:bool
    
    
    def __post_init__(self):
        super().__init__()
    