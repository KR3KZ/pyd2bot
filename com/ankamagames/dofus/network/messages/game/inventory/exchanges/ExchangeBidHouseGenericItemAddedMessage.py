from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseGenericItemAddedMessage(NetworkMessage):
    protocolId = 7602
    objGenericId:int
    
    
