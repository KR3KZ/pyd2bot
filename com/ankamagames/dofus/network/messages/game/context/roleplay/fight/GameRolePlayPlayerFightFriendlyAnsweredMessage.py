from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    

    def init(self, fightId:int, sourceId:int, targetId:int, accept:bool):
        self.fightId = fightId
        self.sourceId = sourceId
        self.targetId = targetId
        self.accept = accept
        
        super().__init__()
    
    