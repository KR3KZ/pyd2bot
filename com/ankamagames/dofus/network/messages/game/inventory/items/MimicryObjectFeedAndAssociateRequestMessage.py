from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    protocolId = 2549
    foodUID:int
    foodPos:int
    preview:bool
    
    
