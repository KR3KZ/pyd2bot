from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeRequestMessage(INetworkMessage):
    protocolId = 289
    exchangeType:int
    
    
