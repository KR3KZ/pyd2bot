from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeRequestedMessage(NetworkMessage):
    protocolId = 5525
    exchangeType:int
    
