from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    challengeId:int
    targetId:int
    

    def init(self, challengeId:int, targetId:int):
        self.challengeId = challengeId
        self.targetId = targetId
        
        super().__init__()
    
    