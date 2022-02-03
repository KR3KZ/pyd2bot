from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import ObtainedItemMessage


class ObtainedItemWithBonusMessage(ObtainedItemMessage):
    bonusQuantity:int
    

    def init(self, bonusQuantity:int, genericId:int, baseQuantity:int):
        self.bonusQuantity = bonusQuantity
        
        super().__init__(genericId, baseQuantity)
    
    