from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsGainMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    
    
