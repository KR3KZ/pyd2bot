from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(INetworkMessage):
    protocolId = 5455
    sellerId:int
    
    
