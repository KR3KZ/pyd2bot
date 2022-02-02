from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class ObjectAddedMessage(NetworkMessage):
    object:ObjectItem
    origin:int
    
    
    def __post_init__(self):
        super().__init__()
    