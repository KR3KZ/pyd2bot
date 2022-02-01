from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountDataErrorMessage(INetworkMessage):
    protocolId = 24
    reason:int
    
    
