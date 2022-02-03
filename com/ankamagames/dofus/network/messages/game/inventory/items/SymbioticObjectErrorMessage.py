from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import ObjectErrorMessage


class SymbioticObjectErrorMessage(ObjectErrorMessage):
    errorCode:int
    

    def init(self, errorCode:int, reason:int):
        self.errorCode = errorCode
        
        super().__init__(reason)
    
    