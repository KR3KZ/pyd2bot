from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeIsReadyMessage(INetworkMessage):
    protocolId = 6263
    id:int
    ready:bool
    
    
