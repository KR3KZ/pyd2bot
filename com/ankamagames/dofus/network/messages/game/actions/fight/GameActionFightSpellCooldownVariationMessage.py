from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    value:int
    
    
