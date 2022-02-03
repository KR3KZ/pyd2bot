from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
    leaderName:str
    nbConnectedMembers:int
    nbTaxCollectors:int
    

    def init(self, leaderName:str, nbConnectedMembers:int, nbTaxCollectors:int, leaderId:int, nbMembers:int, lastActivityDay:int, recruitment:'GuildRecruitmentInformation', nbPendingApply:int, guildEmblem:'GuildEmblem', guildId:int, guildName:str, guildLevel:int):
        self.leaderName = leaderName
        self.nbConnectedMembers = nbConnectedMembers
        self.nbTaxCollectors = nbTaxCollectors
        
        super().__init__(leaderId, nbMembers, lastActivityDay, recruitment, nbPendingApply, guildEmblem, guildId, guildName, guildLevel)
    
    