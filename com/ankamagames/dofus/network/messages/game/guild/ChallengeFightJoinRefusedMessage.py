from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeFightJoinRefusedMessage(NetworkMessage):
    playerId:int
    reason:int
    

    def init(self, playerId:int, reason:int):
        self.playerId = playerId
        self.reason = reason
        
        super().__init__()
    
    