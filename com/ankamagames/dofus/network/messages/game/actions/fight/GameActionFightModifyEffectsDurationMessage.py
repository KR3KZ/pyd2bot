from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    

    def init(self, targetId:int, delta:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.delta = delta
        
        super().__init__(actionId, sourceId)
    
    