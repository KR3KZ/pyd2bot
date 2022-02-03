from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    waitAckId:int
    

    def init(self, waitAckId:int, actionId:int, sourceId:int):
        self.waitAckId = waitAckId
        
        super().__init__(actionId, sourceId)
    
    