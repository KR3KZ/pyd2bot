from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class UpdateLifePointsMessage(INetworkMessage):
    protocolId = 1857
    lifePoints:int
    maxLifePoints:int
    
    
