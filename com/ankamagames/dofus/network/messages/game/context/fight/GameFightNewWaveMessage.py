from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    

    def init(self, id:int, teamId:int, nbTurnBeforeNextWave:int):
        self.id = id
        self.teamId = teamId
        self.nbTurnBeforeNextWave = nbTurnBeforeNextWave
        
        super().__init__()
    
    