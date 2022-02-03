from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSelectionMessage(NetworkMessage):
    serverId:int
    

    def init(self, serverId:int):
        self.serverId = serverId
        
        super().__init__()
    
    