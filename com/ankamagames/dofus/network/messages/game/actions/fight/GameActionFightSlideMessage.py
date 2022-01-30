from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    protocolId = 914
    targetId:int
    startCellId:int
    endCellId:int
    
    
