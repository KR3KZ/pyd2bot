from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    fightId:int
    alliesId:list[int]
    duration:int
    

    def init(self, fightId:int, alliesId:list[int], duration:int):
        self.fightId = fightId
        self.alliesId = alliesId
        self.duration = duration
        
        super().__init__()
    
    