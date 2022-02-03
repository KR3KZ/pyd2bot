from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceGuildLeavingMessage(NetworkMessage):
    kicked:bool
    guildId:int
    

    def init(self, kicked:bool, guildId:int):
        self.kicked = kicked
        self.guildId = guildId
        
        super().__init__()
    
    