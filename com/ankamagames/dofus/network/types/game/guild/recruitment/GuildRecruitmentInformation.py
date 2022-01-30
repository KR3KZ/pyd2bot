from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildRecruitmentInformation(INetworkMessage):
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
    minLevelFacultative:bool
    minSuccessFacultative:bool
    invalidatedByModeration:bool
    recruitmentAutoLocked:bool
    
    
