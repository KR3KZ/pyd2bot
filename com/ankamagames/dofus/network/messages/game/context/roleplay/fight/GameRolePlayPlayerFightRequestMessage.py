from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    targetId:int
    targetCellId:int
    friendly:bool
    

    def init(self, targetId:int, targetCellId:int, friendly:bool):
        self.targetId = targetId
        self.targetCellId = targetCellId
        self.friendly = friendly
        
        super().__init__()
    
    