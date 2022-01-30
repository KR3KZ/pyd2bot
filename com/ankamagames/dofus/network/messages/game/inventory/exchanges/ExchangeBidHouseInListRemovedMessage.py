from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    protocolId = 3610
    itemUID:int
    objectGID:int
    objectType:int
    
