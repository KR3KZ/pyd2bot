from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightPlayersEnemyRemoveMessage(NetworkMessage):
    fightId:int
    playerId:int
    

    def init(self, fightId:int, playerId:int):
        self.fightId = fightId
        self.playerId = playerId
        
        super().__init__()
    
    