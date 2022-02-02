from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SellerBuyerDescriptor(NetworkMessage):
    quantities:list[int]
    types:list[int]
    taxPercentage:int
    taxModificationPercentage:int
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    
    
    def __post_init__(self):
        super().__init__()
    