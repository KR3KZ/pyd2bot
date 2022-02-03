from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateRequestMessage(NetworkMessage):
    permissions:int
    

    def init(self, permissions:int):
        self.permissions = permissions
        
        super().__init__()
    
    