from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeErrorMessage(NetworkMessage):
    protocolId = 6446
    errorType:int
    
    
