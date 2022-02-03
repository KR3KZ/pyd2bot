from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFactsRequestMessage(NetworkMessage):
    guildId:int
    

    def init(self, guildId:int):
        self.guildId = guildId
        
        super().__init__()
    
    