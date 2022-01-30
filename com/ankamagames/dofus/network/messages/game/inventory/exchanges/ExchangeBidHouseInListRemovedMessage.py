from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseInListRemovedMessage(INetworkMessage):
    protocolId = 3610
    itemUID:int
    objectGID:int
    objectType:int
    
    
