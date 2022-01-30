from com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import UpdateLifePointsMessage


class LifePointsRegenEndMessage(UpdateLifePointsMessage):
    protocolId = 5501
    lifePointsGained:int
    
    
