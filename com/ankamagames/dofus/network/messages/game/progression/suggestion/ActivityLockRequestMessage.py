from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActivityLockRequestMessage(NetworkMessage):
    protocolId = 579
    activityId:int
    lock:bool
    
