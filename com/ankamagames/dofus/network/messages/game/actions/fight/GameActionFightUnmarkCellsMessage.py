from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightUnmarkCellsMessage(AbstractGameActionMessage):
    markId:int
    

    def init(self, markId:int, actionId:int, sourceId:int):
        self.markId = markId
        
        super().__init__(actionId, sourceId)
    
    