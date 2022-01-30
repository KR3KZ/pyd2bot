from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(INetworkMessage):
    protocolId = 9780
    objGenericId:int
    
    
