from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    fightId:int
    teamId:int
    option:int
    state:bool
    

    def init(self, fightId:int, teamId:int, option:int, state:bool):
        self.fightId = fightId
        self.teamId = teamId
        self.option = option
        self.state = state
        
        super().__init__()
    
    