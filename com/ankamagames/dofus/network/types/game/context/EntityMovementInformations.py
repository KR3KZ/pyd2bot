from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityMovementInformations(NetworkMessage):
    id:int
    steps:list[int]
    

    def init(self, id:int, steps:list[int]):
        self.id = id
        self.steps = steps
        
        super().__init__()
    
    