from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseGenericItemAddedMessage(INetworkMessage):
    protocolId = 7602
    objGenericId:int
    
    
