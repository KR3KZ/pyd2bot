from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightKillMessage(AbstractGameActionMessage):
    protocolId = 8091
    targetId:int
    
