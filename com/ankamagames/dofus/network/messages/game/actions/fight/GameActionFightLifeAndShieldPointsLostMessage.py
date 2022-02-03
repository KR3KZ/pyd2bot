from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage


class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
    shieldLoss:int
    

    def init(self, shieldLoss:int, targetId:int, loss:int, permanentDamages:int, elementId:int, actionId:int, sourceId:int):
        self.shieldLoss = shieldLoss
        
        super().__init__(targetId, loss, permanentDamages, elementId, actionId, sourceId)
    
    