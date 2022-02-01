from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightStealKamaMessage(AbstractGameActionMessage):
    targetId:int
    amount:int
    
    
