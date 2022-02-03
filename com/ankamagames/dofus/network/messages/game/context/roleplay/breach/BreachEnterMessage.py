from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachEnterMessage(NetworkMessage):
    owner:int
    

    def init(self, owner:int):
        self.owner = owner
        
        super().__init__()
    
    