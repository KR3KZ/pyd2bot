from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationWarningMessage(NetworkMessage):
    battleMode:int
    

    def init(self, battleMode:int):
        self.battleMode = battleMode
        
        super().__init__()
    
    