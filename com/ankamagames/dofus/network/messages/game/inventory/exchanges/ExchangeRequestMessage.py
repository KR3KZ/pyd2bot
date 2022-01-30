from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeRequestMessage(NetworkMessage):
    protocolId = 289
    exchangeType:int
    
