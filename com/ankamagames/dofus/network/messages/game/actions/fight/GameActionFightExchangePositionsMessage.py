from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
    protocolId = 8844
    targetId:float
    casterCellId:int
    targetCellId:int
    
