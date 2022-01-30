from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildRecruitmentInformation(NetworkMessage):
    protocolId = 4584
    guildId:int
    recruitmentType:int
    recruitmentTitle:str
    recruitmentText:str
    selectedLanguages:int
    selectedCriterion:int
    minLevel:int
    minSuccess:int
    lastEditPlayerName:str
    lastEditDate:int
    
