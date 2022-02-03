from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildLevelUpMessage(NetworkMessage):
    newLevel:int
    

    def init(self, newLevel:int):
        self.newLevel = newLevel
        
        super().__init__()
    
    