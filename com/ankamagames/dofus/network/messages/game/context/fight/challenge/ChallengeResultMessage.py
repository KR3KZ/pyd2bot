from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeResultMessage(NetworkMessage):
    challengeId:int
    success:bool
    

    def init(self, challengeId:int, success:bool):
        self.challengeId = challengeId
        self.success = success
        
        super().__init__()
    
    