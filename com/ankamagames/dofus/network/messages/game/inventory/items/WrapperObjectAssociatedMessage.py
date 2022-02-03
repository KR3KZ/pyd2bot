from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage


class WrapperObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
    

    def init(self, hostUID:int):
        
        super().__init__(hostUID)
    
    