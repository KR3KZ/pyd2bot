from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


class ExchangeGuildTaxCollectorGetMessage(NetworkMessage):
    protocolId = 962
    collectorName:str
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    userName:str
    callerId:float
    callerName:str
    experience:float
    pods:int
    objectsInfos:list[ObjectItemGenericQuantity]
    
