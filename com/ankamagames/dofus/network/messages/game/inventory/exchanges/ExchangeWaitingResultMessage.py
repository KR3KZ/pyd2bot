from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeWaitingResultMessage(NetworkMessage):
    protocolId = 4369
    bwait:bool
    
    
