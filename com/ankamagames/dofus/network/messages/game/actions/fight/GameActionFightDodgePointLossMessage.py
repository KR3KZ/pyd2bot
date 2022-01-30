from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDodgePointLossMessage(AbstractGameActionMessage):
    protocolId = 7629
    targetId:float
    amount:int
    
