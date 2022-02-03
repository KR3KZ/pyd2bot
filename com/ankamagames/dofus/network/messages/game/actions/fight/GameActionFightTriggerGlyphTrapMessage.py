from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    markImpactCell:int
    triggeringCharacterId:int
    triggeredSpellId:int
    

    def init(self, markId:int, markImpactCell:int, triggeringCharacterId:int, triggeredSpellId:int, actionId:int, sourceId:int):
        self.markId = markId
        self.markImpactCell = markImpactCell
        self.triggeringCharacterId = triggeringCharacterId
        self.triggeredSpellId = triggeredSpellId
        
        super().__init__(actionId, sourceId)
    
    