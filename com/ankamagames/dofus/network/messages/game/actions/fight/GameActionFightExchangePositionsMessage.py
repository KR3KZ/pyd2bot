from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
    targetId:int
    casterCellId:int
    targetCellId:int
    

    def init(self, targetId:int, casterCellId:int, targetCellId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.casterCellId = casterCellId
        self.targetCellId = targetCellId
        
        super().__init__(actionId, sourceId)
    
    