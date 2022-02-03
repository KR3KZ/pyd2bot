from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCharacterMessage(ObjectUseMessage):
    characterId:int
    

    def init(self, characterId:int, objectUID:int):
        self.characterId = characterId
        
        super().__init__(objectUID)
    
    