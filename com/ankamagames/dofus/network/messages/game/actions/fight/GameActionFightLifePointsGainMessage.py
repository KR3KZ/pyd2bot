from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsGainMessage(AbstractGameActionMessage):
    protocolId = 6777
    targetId:int
    delta:int
    
