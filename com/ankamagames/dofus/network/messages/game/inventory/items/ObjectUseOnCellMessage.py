from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCellMessage(ObjectUseMessage):
    protocolId = 5623
    cells:int
    
    
