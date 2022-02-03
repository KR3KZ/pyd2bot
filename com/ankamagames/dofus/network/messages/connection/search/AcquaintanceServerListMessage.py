from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AcquaintanceServerListMessage(NetworkMessage):
    servers:list[int]
    

    def init(self, servers:list[int]):
        self.servers = servers
        
        super().__init__()
    
    