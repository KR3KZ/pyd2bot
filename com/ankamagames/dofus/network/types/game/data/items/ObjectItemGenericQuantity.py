from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class ObjectItemGenericQuantity(Item):
    objectGID:int
    quantity:int
    

    def init(self, objectGID:int, quantity:int):
        self.objectGID = objectGID
        self.quantity = quantity
        
        super().__init__()
    
    