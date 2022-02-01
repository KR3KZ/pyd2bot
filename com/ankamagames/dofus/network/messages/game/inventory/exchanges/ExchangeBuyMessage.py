from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBuyMessage(INetworkMessage):
    protocolId = 9589
    objectToBuyId:int
    quantity:int
    
    
