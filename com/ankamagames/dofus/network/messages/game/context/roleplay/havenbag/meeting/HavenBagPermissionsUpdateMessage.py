from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateMessage(NetworkMessage):
    permissions:int
    

    def init(self, permissions:int):
        self.permissions = permissions
        
        super().__init__()
    
    