from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    markImpactCell:int
    triggeringCharacterId:int
    triggeredSpellId:int
    
    
