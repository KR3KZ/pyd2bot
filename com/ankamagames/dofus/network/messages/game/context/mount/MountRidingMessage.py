from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRidingMessage(NetworkMessage):
    isRiding:bool
    isAutopilot:bool
    

    def init(self):
        
        super().__init__()
    
    