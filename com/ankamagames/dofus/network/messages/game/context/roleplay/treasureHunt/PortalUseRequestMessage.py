from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PortalUseRequestMessage(INetworkMessage):
    protocolId = 1831
    portalId:int
    
    
