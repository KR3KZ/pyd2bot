from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    fightType:int
    fightId:int
    attackerId:int
    defenderId:int
    containsBoss:bool
    

    def init(self, fightType:int, fightId:int, attackerId:int, defenderId:int, containsBoss:bool):
        self.fightType = fightType
        self.fightId = fightId
        self.attackerId = attackerId
        self.defenderId = defenderId
        self.containsBoss = containsBoss
        
        super().__init__()
    
    