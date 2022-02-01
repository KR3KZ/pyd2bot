from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBuyMessage(NetworkMessage):
    objectToBuyId:int
    quantity:int
    
    
