from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MigratedServerListMessage(NetworkMessage):
    migratedServerIds:list[int]
    

    def init(self, migratedServerIds:list[int]):
        self.migratedServerIds = migratedServerIds
        
        super().__init__()
    
    