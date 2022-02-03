from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenamedMessage(NetworkMessage):
    mountId:int
    name:str
    

    def init(self, mountId:int, name:str):
        self.mountId = mountId
        self.name = name
        
        super().__init__()
    
    