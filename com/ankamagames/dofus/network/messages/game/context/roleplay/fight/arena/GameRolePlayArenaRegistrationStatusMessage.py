from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    registered:bool
    step:int
    battleMode:int
    

    def init(self, registered:bool, step:int, battleMode:int):
        self.registered = registered
        self.step = step
        self.battleMode = battleMode
        
        super().__init__()
    
    