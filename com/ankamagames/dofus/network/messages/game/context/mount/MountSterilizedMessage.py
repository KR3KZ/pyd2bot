from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountSterilizedMessage(NetworkMessage):
    mountId:int
    

    def init(self, mountId:int):
        self.mountId = mountId
        
        super().__init__()
    
    