from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayAggressionMessage(NetworkMessage):
    attackerId:int
    defenderId:int
    

    def init(self, attackerId:int, defenderId:int):
        self.attackerId = attackerId
        self.defenderId = defenderId
        
        super().__init__()
    
    