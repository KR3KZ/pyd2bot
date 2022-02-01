from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    foodUID:int
    foodPos:int
    preview:bool
    
    
