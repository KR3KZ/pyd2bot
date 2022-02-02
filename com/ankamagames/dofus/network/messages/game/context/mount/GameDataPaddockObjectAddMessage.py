from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


@dataclass
class GameDataPaddockObjectAddMessage(NetworkMessage):
    paddockItemDescription:PaddockItem
    
    
    def __post_init__(self):
        super().__init__()
    