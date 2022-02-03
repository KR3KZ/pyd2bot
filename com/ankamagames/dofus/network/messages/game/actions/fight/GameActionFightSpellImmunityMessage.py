from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellImmunityMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    

    def init(self, targetId:int, spellId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.spellId = spellId
        
        super().__init__(actionId, sourceId)
    
    