from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCharacterMessage(ObjectUseMessage):
    protocolId = 8768
    characterId:int
    
    
