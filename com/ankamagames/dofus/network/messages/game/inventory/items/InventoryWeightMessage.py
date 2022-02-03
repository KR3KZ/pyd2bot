from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InventoryWeightMessage(NetworkMessage):
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    

    def init(self, inventoryWeight:int, shopWeight:int, weightMax:int):
        self.inventoryWeight = inventoryWeight
        self.shopWeight = shopWeight
        self.weightMax = weightMax
        
        super().__init__()
    
    