from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuestLimitationMessage(INetworkMessage):
    protocolId = 1036
    reason:int
    
    
