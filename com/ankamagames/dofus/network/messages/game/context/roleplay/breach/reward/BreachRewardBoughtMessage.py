from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRewardBoughtMessage(NetworkMessage):
    id:int
    bought:bool
    

    def init(self, id:int, bought:bool):
        self.id = id
        self.bought = bought
        
        super().__init__()
    
    