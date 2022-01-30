from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightThrowCharacterMessage(AbstractGameActionMessage):
    protocolId = 1069
    targetId:float
    cellId:int
    
