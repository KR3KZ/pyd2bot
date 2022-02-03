from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivityHideRequestMessage(NetworkMessage):
    activityId:int
    

    def init(self, activityId:int):
        self.activityId = activityId
        
        super().__init__()
    
    