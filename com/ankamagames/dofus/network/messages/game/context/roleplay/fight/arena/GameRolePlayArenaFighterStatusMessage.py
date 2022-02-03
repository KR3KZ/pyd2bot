from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    fightId:int
    playerId:int
    accepted:bool
    

    def init(self, fightId:int, playerId:int, accepted:bool):
        self.fightId = fightId
        self.playerId = playerId
        self.accepted = accepted
        
        super().__init__()
    
    