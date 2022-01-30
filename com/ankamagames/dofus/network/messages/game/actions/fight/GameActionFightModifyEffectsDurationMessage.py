from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    protocolId = 7980
    targetId:int
    delta:int
    
