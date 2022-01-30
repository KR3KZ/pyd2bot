from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightStealKamaMessage(AbstractGameActionMessage):
    protocolId = 8847
    targetId:int
    amount:int
    
    
