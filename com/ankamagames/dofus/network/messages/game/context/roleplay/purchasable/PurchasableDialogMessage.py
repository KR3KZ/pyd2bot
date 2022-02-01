from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    purchasableId:int
    purchasableInstanceId:int
    price:int
    buyOrSell:bool
    secondHand:bool
    
    
