from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReduceDamagesMessage(AbstractGameActionMessage):
    protocolId = 3304
    targetId:int
    amount:int
    
