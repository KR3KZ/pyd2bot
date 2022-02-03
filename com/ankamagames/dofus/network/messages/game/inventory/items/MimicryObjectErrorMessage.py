from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage


class MimicryObjectErrorMessage(SymbioticObjectErrorMessage):
    preview:bool
    

    def init(self, preview:bool, errorCode:int, reason:int):
        self.preview = preview
        
        super().__init__(errorCode, reason)
    
    