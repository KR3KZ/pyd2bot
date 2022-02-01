from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellImmunityMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    
    
