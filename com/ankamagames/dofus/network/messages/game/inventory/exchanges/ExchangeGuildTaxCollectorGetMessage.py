from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


@dataclass
class ExchangeGuildTaxCollectorGetMessage(NetworkMessage):
    collectorName:str
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    userName:str
    callerId:int
    callerName:str
    experience:int
    pods:int
    objectsInfos:list[ObjectItemGenericQuantity]
    
    
    def __post_init__(self):
        super().__init__()
    