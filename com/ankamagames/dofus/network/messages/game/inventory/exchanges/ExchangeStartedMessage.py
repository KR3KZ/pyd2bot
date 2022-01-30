from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartedMessage(NetworkMessage):
    protocolId = 8540
    exchangeType:int
    
