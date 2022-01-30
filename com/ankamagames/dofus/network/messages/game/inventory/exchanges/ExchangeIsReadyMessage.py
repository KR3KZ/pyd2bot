from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeIsReadyMessage(NetworkMessage):
    protocolId = 6263
    id:int
    ready:bool
    
