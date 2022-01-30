from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartedMessage(INetworkMessage):
    protocolId = 8540
    exchangeType:int
    
    
