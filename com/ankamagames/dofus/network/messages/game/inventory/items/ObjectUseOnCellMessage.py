from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCellMessage(ObjectUseMessage):
    cells:int
    

    def init(self, cells:int, objectUID:int):
        self.cells = cells
        
        super().__init__(objectUID)
    
    