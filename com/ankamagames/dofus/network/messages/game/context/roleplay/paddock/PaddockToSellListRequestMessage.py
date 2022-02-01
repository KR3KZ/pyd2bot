from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockToSellListRequestMessage(INetworkMessage):
    protocolId = 456
    pageIndex:int
    
    
