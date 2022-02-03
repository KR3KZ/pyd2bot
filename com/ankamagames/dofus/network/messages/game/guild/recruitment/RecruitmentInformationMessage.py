from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    


class RecruitmentInformationMessage(NetworkMessage):
    recruitmentData:'GuildRecruitmentInformation'
    

    def init(self, recruitmentData:'GuildRecruitmentInformation'):
        self.recruitmentData = recruitmentData
        
        super().__init__()
    
    