from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
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
    objectsInfos:list['ObjectItemGenericQuantity']
    

    def init(self, collectorName:str, worldX:int, worldY:int, mapId:int, subAreaId:int, userName:str, callerId:int, callerName:str, experience:int, pods:int, objectsInfos:list['ObjectItemGenericQuantity']):
        self.collectorName = collectorName
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.userName = userName
        self.callerId = callerId
        self.callerName = callerName
        self.experience = experience
        self.pods = pods
        self.objectsInfos = objectsInfos
        
        super().__init__()
    
    