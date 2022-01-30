from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightInvisibleDetectedMessage(AbstractGameActionMessage):
    protocolId = 5294
    targetId:float
    cellId:int
    
