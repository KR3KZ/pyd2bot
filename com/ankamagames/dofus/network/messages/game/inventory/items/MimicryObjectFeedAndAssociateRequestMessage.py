from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    foodUID:int
    foodPos:int
    preview:bool
    

    def init(self, foodUID:int, foodPos:int, preview:bool, symbioteUID:int, symbiotePos:int, hostUID:int, hostPos:int):
        self.foodUID = foodUID
        self.foodPos = foodPos
        self.preview = preview
        
        super().__init__(symbioteUID, symbiotePos, hostUID, hostPos)
    
    