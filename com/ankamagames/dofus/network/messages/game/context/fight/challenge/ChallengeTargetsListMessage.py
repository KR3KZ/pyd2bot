from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetsListMessage(NetworkMessage):
    targetIds:list[int]
    targetCells:list[int]
    

    def init(self, targetIds:list[int], targetCells:list[int]):
        self.targetIds = targetIds
        self.targetCells = targetCells
        
        super().__init__()
    
    