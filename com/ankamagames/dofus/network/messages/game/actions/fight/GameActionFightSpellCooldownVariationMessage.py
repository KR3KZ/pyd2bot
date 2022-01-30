from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    protocolId = 2288
    targetId:int
    spellId:int
    value:int
    
    
