from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActivityLockRequestMessage(INetworkMessage):
    protocolId = 579
    activityId:int
    lock:bool
    
    
