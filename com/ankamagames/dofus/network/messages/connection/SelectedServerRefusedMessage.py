from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    serverId:int
    error:int
    serverStatus:int
    

    def init(self, serverId:int, error:int, serverStatus:int):
        self.serverId = serverId
        self.error = error
        self.serverStatus = serverStatus
        
        super().__init__()
    
    