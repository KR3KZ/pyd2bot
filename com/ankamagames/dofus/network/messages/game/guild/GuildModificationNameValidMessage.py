from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildModificationNameValidMessage(NetworkMessage):
    guildName:str
    

    def init(self, guildName:str):
        self.guildName = guildName
        
        super().__init__()
    
    