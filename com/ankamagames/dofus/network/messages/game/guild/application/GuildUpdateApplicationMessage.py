from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildUpdateApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    

    def init(self, applyText:str, guildId:int):
        self.applyText = applyText
        self.guildId = guildId
        
        super().__init__()
    
    