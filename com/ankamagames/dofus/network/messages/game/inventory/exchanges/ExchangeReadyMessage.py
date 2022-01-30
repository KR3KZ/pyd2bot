from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeReadyMessage(INetworkMessage):
    protocolId = 5849
    ready:bool
    step:int
    
    
