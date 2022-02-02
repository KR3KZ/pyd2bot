from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem


@dataclass
class EvolutiveObjectRecycleResultMessage(NetworkMessage):
    recycledItems:list[RecycledItem]
    
    
    def __post_init__(self):
        super().__init__()
    