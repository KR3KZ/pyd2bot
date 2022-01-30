from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ErrorMapNotFoundMessage(NetworkMessage):
    protocolId = 1147
    mapId:int
    
    
