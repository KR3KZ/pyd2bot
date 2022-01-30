from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ErrorMapNotFoundMessage(INetworkMessage):
    protocolId = 1147
    mapId:int
    
    
