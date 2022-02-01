from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ErrorMapNotFoundMessage(INetworkMessage):
    protocolId = 1147
    mapId:int
    
    
