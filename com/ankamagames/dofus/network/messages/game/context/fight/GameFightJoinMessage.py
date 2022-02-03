from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    

    def init(self, timeMaxBeforeFightStart:int, fightType:int):
        self.timeMaxBeforeFightStart = timeMaxBeforeFightStart
        self.fightType = fightType
        
        super().__init__()
    
    