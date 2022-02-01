from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseGenericItemAddedMessage(INetworkMessage):
    protocolId = 7602
    objGenericId:int
    
    
