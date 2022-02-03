from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


class GuildInAllianceVersatileInformations(GuildVersatileInformations):
    allianceId:int
    

    def init(self, allianceId:int, guildId:int, leaderId:int, guildLevel:int, nbMembers:int):
        self.allianceId = allianceId
        
        super().__init__(guildId, leaderId, guildLevel, nbMembers)
    
    