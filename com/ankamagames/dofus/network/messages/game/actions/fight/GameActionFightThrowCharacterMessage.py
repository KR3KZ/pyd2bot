from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightThrowCharacterMessage(AbstractGameActionMessage):
    targetId:int
    cellId:int
    
    
