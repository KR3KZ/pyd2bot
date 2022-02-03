from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityInformation(NetworkMessage):
    id:int
    experience:int
    status:bool
    

    def init(self, id:int, experience:int, status:bool):
        self.id = id
        self.experience = experience
        self.status = status
        
        super().__init__()
    
    