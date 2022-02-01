from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockBuyResultMessage(INetworkMessage):
    protocolId = 6835
    paddockId:int
    bought:bool
    realPrice:int
    
    
