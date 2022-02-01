from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountXpRatioMessage(INetworkMessage):
    protocolId = 1527
    ratio:int
    
    
