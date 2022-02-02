from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


@dataclass
class GuildFactSheetInformations(GuildInformations):
    leaderId:int
    nbMembers:int
    lastActivityDay:int
    recruitment:GuildRecruitmentInformation
    nbPendingApply:int
    
    
    def __post_init__(self):
        super().__init__()
    