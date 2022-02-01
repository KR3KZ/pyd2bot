from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseToSellListRequestMessage(INetworkMessage):
    protocolId = 1679
    pageIndex:int
    
    
