from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorBasicInformations(NetworkMessage):
    protocolId = 1488
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    
