from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MapInformationsRequestMessage(INetworkMessage):
    protocolId = 2396
    mapId:int
    
    
