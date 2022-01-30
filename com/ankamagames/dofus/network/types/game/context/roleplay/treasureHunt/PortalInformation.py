from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PortalInformation(INetworkMessage):
    protocolId = 2145
    portalId:int
    areaId:int
    
    
