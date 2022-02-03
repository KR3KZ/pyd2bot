from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    purchasableId:int
    purchasableInstanceId:int
    price:int
    buyOrSell:bool
    secondHand:bool
    

    def init(self, purchasableId:int, purchasableInstanceId:int, price:int):
        self.purchasableId = purchasableId
        self.purchasableInstanceId = purchasableInstanceId
        self.price = price
        
        super().__init__()
    
    