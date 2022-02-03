from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceChangeGuildRightsMessage(NetworkMessage):
    guildId:int
    rights:int
    

    def init(self, guildId:int, rights:int):
        self.guildId = guildId
        self.rights = rights
        
        super().__init__()
    
    