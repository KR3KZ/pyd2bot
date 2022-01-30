from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TaxCollectorBasicInformations(INetworkMessage):
    protocolId = 1488
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
