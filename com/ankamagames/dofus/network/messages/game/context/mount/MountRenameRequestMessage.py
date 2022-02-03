from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenameRequestMessage(NetworkMessage):
    name:str
    mountId:int
    

    def init(self, name:str, mountId:int):
        self.name = name
        self.mountId = mountId
        
        super().__init__()
    
    