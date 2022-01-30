from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LifePointsRegenBeginMessage(INetworkMessage):
    protocolId = 9626
    regenRate:int
    
    
