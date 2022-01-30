from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import ObjectErrorMessage


class SymbioticObjectErrorMessage(ObjectErrorMessage):
    protocolId = 8441
    errorCode:int
    
    
