from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


class RecruitmentInformationMessage(NetworkMessage):
    protocolId = 3164
    recruitmentData:GuildRecruitmentInformation
    
    
