from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MonsterBoosts(NetworkMessage):
    id:int
    xpBoost:int
    dropBoost:int
    

    def init(self, id:int, xpBoost:int, dropBoost:int):
        self.id = id
        self.xpBoost = xpBoost
        self.dropBoost = dropBoost
        
        super().__init__()
    
    