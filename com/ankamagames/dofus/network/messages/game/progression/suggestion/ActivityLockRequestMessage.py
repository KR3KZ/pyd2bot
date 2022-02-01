from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivityLockRequestMessage(NetworkMessage):
    activityId:int
    lock:bool
    
    
