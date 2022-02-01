from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    uid:int
    qty:int
    price:int
    
    
