from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellBuyDialogMessage(NetworkMessage):
    bsell:bool
    ownerId:int
    price:int
    
    
