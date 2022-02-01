from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    
    
