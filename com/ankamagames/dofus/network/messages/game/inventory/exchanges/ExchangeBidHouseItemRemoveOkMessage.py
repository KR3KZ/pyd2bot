from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(NetworkMessage):
    protocolId = 5455
    sellerId:int
    
    
