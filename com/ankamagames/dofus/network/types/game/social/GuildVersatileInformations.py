from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildVersatileInformations(NetworkMessage):
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    

    def init(self, guildId:int, leaderId:int, guildLevel:int, nbMembers:int):
        self.guildId = guildId
        self.leaderId = leaderId
        self.guildLevel = guildLevel
        self.nbMembers = nbMembers
        
        super().__init__()
    
    