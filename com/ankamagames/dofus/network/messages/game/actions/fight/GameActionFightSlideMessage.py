from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    protocolId = 914
    targetId:float
    startCellId:int
    endCellId:int
    
