from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class UpdateLifePointsMessage(NetworkMessage):
    protocolId = 1857
    lifePoints:int
    maxLifePoints:int
    
