from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeHandleMountsMessage(INetworkMessage):
    protocolId = 9421
    actionType:int
    ridesId:int
    
    
