from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaPlayerBehavioursMessage(NetworkMessage):
    flags:list[str]
    sanctions:list[str]
    banDuration:int
    

    def init(self, flags:list[str], sanctions:list[str], banDuration:int):
        self.flags = flags
        self.sanctions = sanctions
        self.banDuration = banDuration
        
        super().__init__()
    
    