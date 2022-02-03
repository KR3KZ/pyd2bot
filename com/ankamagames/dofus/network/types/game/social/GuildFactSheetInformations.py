from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildFactSheetInformations(GuildInformations):
    leaderId:int
    nbMembers:int
    lastActivityDay:int
    recruitment:'GuildRecruitmentInformation'
    nbPendingApply:int
    

    def init(self, leaderId:int, nbMembers:int, lastActivityDay:int, recruitment:'GuildRecruitmentInformation', nbPendingApply:int, guildEmblem:'GuildEmblem', guildId:int, guildName:str, guildLevel:int):
        self.leaderId = leaderId
        self.nbMembers = nbMembers
        self.lastActivityDay = lastActivityDay
        self.recruitment = recruitment
        self.nbPendingApply = nbPendingApply
        
        super().__init__(guildEmblem, guildId, guildName, guildLevel)
    
    