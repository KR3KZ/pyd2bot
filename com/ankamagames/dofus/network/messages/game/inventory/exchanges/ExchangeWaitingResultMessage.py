from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeWaitingResultMessage(INetworkMessage):
    protocolId = 4369
    bwait:bool
    
    
