from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeSellMessage(NetworkMessage):
    objectToSellId:int
    quantity:int
    
    
