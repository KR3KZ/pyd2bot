from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class ObjectItemQuantity(Item):
    objectUID:int
    quantity:int
    

    def init(self, objectUID:int, quantity:int):
        self.objectUID = objectUID
        self.quantity = quantity
        
        super().__init__()
    
    