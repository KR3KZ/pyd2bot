from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    

    def init(self, challengeId:int, targetId:int, xpBonus:int, dropBonus:int):
        self.challengeId = challengeId
        self.targetId = targetId
        self.xpBonus = xpBonus
        self.dropBonus = dropBonus
        
        super().__init__()
    
    