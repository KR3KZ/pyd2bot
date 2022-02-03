from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
    targetId:int
    loss:int
    permanentDamages:int
    elementId:int
    

    def init(self, targetId:int, loss:int, permanentDamages:int, elementId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.loss = loss
        self.permanentDamages = permanentDamages
        self.elementId = elementId
        
        super().__init__(actionId, sourceId)
    
    