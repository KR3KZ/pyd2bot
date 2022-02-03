from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildJoinAutomaticallyRequestMessage(NetworkMessage):
    guildId:int
    

    def init(self, guildId:int):
        self.guildId = guildId
        
        super().__init__()
    
    