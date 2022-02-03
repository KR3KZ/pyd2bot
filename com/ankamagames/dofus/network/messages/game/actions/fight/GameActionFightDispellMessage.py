from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    targetId:int
    verboseCast:bool
    

    def init(self, targetId:int, verboseCast:bool, actionId:int, sourceId:int):
        self.targetId = targetId
        self.verboseCast = verboseCast
        
        super().__init__(actionId, sourceId)
    
    