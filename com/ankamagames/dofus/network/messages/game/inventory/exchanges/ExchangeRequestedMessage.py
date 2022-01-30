from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeRequestedMessage(INetworkMessage):
    protocolId = 5525
    exchangeType:int
    
    
