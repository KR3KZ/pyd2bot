from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PortalInformation(NetworkMessage):
    protocolId = 2145
    portalId:int
    areaId:int
    
    
