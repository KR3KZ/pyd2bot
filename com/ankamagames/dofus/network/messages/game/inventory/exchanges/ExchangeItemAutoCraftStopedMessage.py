from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeItemAutoCraftStopedMessage(INetworkMessage):
    protocolId = 470
    reason:int
    
    
