from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PortalUseRequestMessage(INetworkMessage):
    protocolId = 1831
    portalId:int
    
    
