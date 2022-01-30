from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellImmunityMessage(AbstractGameActionMessage):
    protocolId = 7640
    targetId:int
    spellId:int
    
    
