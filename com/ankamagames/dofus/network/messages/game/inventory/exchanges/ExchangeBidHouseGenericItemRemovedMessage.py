from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(INetworkMessage):
    protocolId = 9780
    objGenericId:int
    
    
