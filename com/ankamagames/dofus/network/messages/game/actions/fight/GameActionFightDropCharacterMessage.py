from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDropCharacterMessage(AbstractGameActionMessage):
    targetId:int
    cellId:int
    
    
