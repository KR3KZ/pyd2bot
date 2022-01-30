from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeItemAutoCraftStopedMessage(NetworkMessage):
    protocolId = 470
    reason:int
    
