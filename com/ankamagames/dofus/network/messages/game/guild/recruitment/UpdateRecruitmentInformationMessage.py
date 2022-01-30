from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


class UpdateRecruitmentInformationMessage(NetworkMessage):
    protocolId = 3169
    recruitmentData:GuildRecruitmentInformation
    
    
