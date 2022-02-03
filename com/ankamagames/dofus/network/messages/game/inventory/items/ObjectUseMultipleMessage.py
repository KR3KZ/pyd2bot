from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseMultipleMessage(ObjectUseMessage):
    quantity:int
    

    def init(self, quantity:int, objectUID:int):
        self.quantity = quantity
        
        super().__init__(objectUID)
    
    