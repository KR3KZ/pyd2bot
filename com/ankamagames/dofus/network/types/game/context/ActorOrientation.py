from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActorOrientation(NetworkMessage):
    id:int
    direction:int
    

    def init(self, id:int, direction:int):
        self.id = id
        self.direction = direction
        
        super().__init__()
    
    