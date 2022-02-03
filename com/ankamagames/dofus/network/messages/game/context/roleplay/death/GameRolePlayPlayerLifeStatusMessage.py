from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    state:int
    phenixMapId:int
    

    def init(self, state:int, phenixMapId:int):
        self.state = state
        self.phenixMapId = phenixMapId
        
        super().__init__()
    
    