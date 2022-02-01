from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    targetId:int
    startCellId:int
    endCellId:int
    
    
