from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ActivityLockRequestMessage(INetworkMessage):
    protocolId = 579
    activityId:int
    lock:bool
    
    
