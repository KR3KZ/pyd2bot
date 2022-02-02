from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


@dataclass
class PrismsListMessage(NetworkMessage):
    prisms:list[PrismSubareaEmptyInfo]
    
    
    def __post_init__(self):
        super().__init__()
    