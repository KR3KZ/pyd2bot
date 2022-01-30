from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDeathMessage(AbstractGameActionMessage):
    protocolId = 7663
    targetId:int
    
    
