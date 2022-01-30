from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


class ExchangeGuildTaxCollectorGetMessage(INetworkMessage):
    protocolId = 962
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
    objectsInfos:ObjectItemGenericQuantity
    
    
