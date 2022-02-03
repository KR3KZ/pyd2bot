from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    

    def init(self, playerId:int, monsterGroupId:int, angryStartTime:int, attackTime:int):
        self.playerId = playerId
        self.monsterGroupId = monsterGroupId
        self.angryStartTime = angryStartTime
        self.attackTime = attackTime
        
        super().__init__()
    
    