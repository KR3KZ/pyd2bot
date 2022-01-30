from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    protocolId = 1777
    markId:int
    markImpactCell:int
    triggeringCharacterId:float
    triggeredSpellId:int
    
