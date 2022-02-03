from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    targetId:int
    startCellId:int
    endCellId:int
    

    def init(self, targetId:int, startCellId:int, endCellId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.startCellId = startCellId
        self.endCellId = endCellId
        
        super().__init__(actionId, sourceId)
    
    