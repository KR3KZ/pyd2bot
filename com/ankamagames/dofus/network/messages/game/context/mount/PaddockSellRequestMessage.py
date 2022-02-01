from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    price:int
    forSale:bool
    
    
