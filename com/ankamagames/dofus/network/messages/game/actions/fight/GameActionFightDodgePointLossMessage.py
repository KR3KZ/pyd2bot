from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDodgePointLossMessage(AbstractGameActionMessage):
    targetId:int
    amount:int
    
    
