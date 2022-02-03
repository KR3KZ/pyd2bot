from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetsListRequestMessage(NetworkMessage):
    challengeId:int
    

    def init(self, challengeId:int):
        self.challengeId = challengeId
        
        super().__init__()
    
    