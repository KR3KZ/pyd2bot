from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountSetXpRatioRequestMessage(INetworkMessage):
    protocolId = 9275
    xpRatio:int
    
    
