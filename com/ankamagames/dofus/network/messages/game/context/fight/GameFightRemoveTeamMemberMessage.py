from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightRemoveTeamMemberMessage(NetworkMessage):
    fightId:int
    teamId:int
    charId:int
    

    def init(self, fightId:int, teamId:int, charId:int):
        self.fightId = fightId
        self.teamId = teamId
        self.charId = charId
        
        super().__init__()
    
    