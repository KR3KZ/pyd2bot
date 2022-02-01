from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LifePointsRegenBeginMessage(INetworkMessage):
    protocolId = 9626
    regenRate:int
    
    
