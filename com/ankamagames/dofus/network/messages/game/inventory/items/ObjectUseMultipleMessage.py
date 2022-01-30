from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseMultipleMessage(ObjectUseMessage):
    protocolId = 1126
    quantity:int
    
