from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    protocolId = 3195
    uid:int
    qty:int
    price:int
    
