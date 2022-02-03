from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayRemoveChallengeMessage(NetworkMessage):
    fightId:int
    

    def init(self, fightId:int):
        self.fightId = fightId
        
        super().__init__()
    
    