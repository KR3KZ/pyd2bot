from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


class UpdateRecruitmentInformationMessage(NetworkMessage):
    recruitmentData:GuildRecruitmentInformation
    
    
