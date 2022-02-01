from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReduceDamagesMessage(AbstractGameActionMessage):
    targetId:int
    amount:int
    
    
