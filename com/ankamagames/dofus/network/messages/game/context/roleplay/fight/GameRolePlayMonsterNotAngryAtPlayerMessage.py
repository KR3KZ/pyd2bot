from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayMonsterNotAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    

    def init(self, playerId:int, monsterGroupId:int):
        self.playerId = playerId
        self.monsterGroupId = monsterGroupId
        
        super().__init__()
    
    