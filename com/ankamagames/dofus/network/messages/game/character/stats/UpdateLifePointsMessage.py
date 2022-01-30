from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class UpdateLifePointsMessage(INetworkMessage):
    protocolId = 1857
    lifePoints:int
    maxLifePoints:int
    
    
