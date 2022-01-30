from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LifePointsRegenBeginMessage(NetworkMessage):
    protocolId = 9626
    regenRate:int
    
