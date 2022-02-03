from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayFightRequestCanceledMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    

    def init(self, fightId:int, sourceId:int, targetId:int):
        self.fightId = fightId
        self.sourceId = sourceId
        self.targetId = targetId
        
        super().__init__()
    
    