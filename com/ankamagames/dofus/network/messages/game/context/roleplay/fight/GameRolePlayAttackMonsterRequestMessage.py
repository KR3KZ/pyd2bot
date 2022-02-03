from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayAttackMonsterRequestMessage(NetworkMessage):
    monsterGroupId:int
    

    def init(self, monsterGroupId:int):
        self.monsterGroupId = monsterGroupId
        
        super().__init__()
    
    