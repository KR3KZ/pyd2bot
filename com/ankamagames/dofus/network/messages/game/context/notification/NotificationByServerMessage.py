from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    id:int
    parameters:list[str]
    forceOpen:bool
    

    def init(self, id:int, parameters:list[str], forceOpen:bool):
        self.id = id
        self.parameters = parameters
        self.forceOpen = forceOpen
        
        super().__init__()
    
    