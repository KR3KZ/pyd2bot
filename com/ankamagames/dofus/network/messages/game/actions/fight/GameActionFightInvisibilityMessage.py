from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightInvisibilityMessage(AbstractGameActionMessage):
    targetId:int
    state:int
    

    def init(self, targetId:int, state:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.state = state
        
        super().__init__(actionId, sourceId)
    
    