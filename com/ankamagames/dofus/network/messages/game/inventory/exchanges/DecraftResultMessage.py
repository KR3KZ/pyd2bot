from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo


@dataclass
class DecraftResultMessage(NetworkMessage):
    results:list[DecraftedItemStackInfo]
    
    
    def __post_init__(self):
        super().__init__()
    