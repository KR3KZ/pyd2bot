from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(NetworkMessage):
    protocolId = 9780
    objGenericId:int
    
    
