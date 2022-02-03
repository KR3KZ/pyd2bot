from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightNewRoundMessage(NetworkMessage):
    roundNumber:int
    

    def init(self, roundNumber:int):
        self.roundNumber = roundNumber
        
        super().__init__()
    
    