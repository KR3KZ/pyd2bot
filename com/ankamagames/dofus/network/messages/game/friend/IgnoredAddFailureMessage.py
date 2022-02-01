from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IgnoredAddFailureMessage(INetworkMessage):
    protocolId = 4052
    reason:int
    
    
