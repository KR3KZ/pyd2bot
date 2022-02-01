from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateLifePointsMessage(NetworkMessage):
    lifePoints:int
    maxLifePoints:int
    
    
