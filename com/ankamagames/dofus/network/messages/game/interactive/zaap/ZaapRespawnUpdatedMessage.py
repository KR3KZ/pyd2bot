from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ZaapRespawnUpdatedMessage(INetworkMessage):
    protocolId = 2988
    mapId:int
    
    
