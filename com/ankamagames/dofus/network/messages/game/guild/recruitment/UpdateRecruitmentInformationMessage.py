from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


@dataclass
class UpdateRecruitmentInformationMessage(NetworkMessage):
    recruitmentData:GuildRecruitmentInformation
    
    
    def __post_init__(self):
        super().__init__()
    