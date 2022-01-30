from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseBuyMessage(INetworkMessage):
    protocolId = 3195
    uid:int
    qty:int
    price:int
    
    
