from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightAnswerMessage(NetworkMessage):
    fightId:int
    accept:bool
    

    def init(self, fightId:int, accept:bool):
        self.fightId = fightId
        self.accept = accept
        
        super().__init__()
    
    