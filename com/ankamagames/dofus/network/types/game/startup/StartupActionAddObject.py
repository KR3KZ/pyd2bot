from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity


@dataclass
class StartupActionAddObject(NetworkMessage):
    uid:int
    title:str
    text:str
    descUrl:str
    pictureUrl:str
    items:list[ObjectItemInformationWithQuantity]
    
    
    def __post_init__(self):
        super().__init__()
    