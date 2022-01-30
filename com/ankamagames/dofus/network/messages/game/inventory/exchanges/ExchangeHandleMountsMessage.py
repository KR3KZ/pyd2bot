from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeHandleMountsMessage(INetworkMessage):
    protocolId = 9421
    actionType:int
    ridesId:int
    
    
