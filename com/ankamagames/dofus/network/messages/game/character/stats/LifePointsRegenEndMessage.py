from com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import UpdateLifePointsMessage


class LifePointsRegenEndMessage(UpdateLifePointsMessage):
    lifePointsGained:int
    

    def init(self, lifePointsGained:int, lifePoints:int, maxLifePoints:int):
        self.lifePointsGained = lifePointsGained
        
        super().__init__(lifePoints, maxLifePoints)
    
    