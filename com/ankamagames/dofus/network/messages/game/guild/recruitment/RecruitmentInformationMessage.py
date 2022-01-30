from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation


class RecruitmentInformationMessage(INetworkMessage):
    protocolId = 3164
    recruitmentData:GuildRecruitmentInformation
    
    
