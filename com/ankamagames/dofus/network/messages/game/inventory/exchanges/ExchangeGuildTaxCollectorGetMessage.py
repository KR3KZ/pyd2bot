from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


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
    
    
