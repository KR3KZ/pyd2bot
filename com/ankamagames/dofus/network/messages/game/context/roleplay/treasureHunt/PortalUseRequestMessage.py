from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PortalUseRequestMessage(NetworkMessage):
    protocolId = 1831
    portalId:int
    
    
