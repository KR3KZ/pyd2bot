from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportRequestMessage(INetworkMessage):
    protocolId = 1539
    sourceType:int
    destinationType:int
    mapId:int
    
    
