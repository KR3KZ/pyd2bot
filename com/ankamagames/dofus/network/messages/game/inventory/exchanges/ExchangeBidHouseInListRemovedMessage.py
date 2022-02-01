from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseInListRemovedMessage(INetworkMessage):
    protocolId = 3610
    itemUID:int
    objectGID:int
    objectType:int
    
    
