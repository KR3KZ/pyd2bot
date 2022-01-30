from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeErrorMessage(INetworkMessage):
    protocolId = 6446
    errorType:int
    
    
