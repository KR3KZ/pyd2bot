from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(INetworkMessage):
    protocolId = 5455
    sellerId:int
    
    
