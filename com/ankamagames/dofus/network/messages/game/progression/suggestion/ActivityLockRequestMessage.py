from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivityLockRequestMessage(NetworkMessage):
    activityId:int
    lock:bool
    

    def init(self, activityId:int, lock:bool):
        self.activityId = activityId
        self.lock = lock
        
        super().__init__()
    
    