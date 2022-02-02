from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class InventoryWeightMessage(NetworkMessage):
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    
    
    def __post_init__(self):
        super().__init__()
    