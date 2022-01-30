from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
    protocolId = 8844
    targetId:int
    casterCellId:int
    targetCellId:int
    
