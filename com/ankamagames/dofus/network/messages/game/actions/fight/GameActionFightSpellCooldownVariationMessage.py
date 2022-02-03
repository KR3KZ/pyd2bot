from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    value:int
    

    def init(self, targetId:int, spellId:int, value:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.spellId = spellId
        self.value = value
        
        super().__init__(actionId, sourceId)
    
    