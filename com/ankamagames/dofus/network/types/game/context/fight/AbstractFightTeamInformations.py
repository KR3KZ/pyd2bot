from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightTeamInformations(NetworkMessage):
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    

    def init(self, teamId:int, leaderId:int, teamSide:int, teamTypeId:int, nbWaves:int):
        self.teamId = teamId
        self.leaderId = leaderId
        self.teamSide = teamSide
        self.teamTypeId = teamTypeId
        self.nbWaves = nbWaves
        
        super().__init__()
    
    