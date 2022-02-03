from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightJoinRequestMessage(NetworkMessage):
    fighterId:int
    fightId:int
    

    def init(self, fighterId:int, fightId:int):
        self.fighterId = fighterId
        self.fightId = fightId
        
        super().__init__()
    
    