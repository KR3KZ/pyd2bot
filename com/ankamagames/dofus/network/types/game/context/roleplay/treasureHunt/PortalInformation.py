from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PortalInformation(INetworkMessage):
    protocolId = 2145
    portalId:int
    areaId:int
    
    
