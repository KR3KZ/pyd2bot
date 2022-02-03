from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NamedPartyTeam(NetworkMessage):
    teamId:int
    partyName:str
    

    def init(self, teamId:int, partyName:str):
        self.teamId = teamId
        self.partyName = partyName
        
        super().__init__()
    
    