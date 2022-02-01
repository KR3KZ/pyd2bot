from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildRecruitmentInformation(NetworkMessage):
    guildId:int
    recruitmentType:int
    recruitmentTitle:str
    recruitmentText:str
    selectedLanguages:list[int]
    selectedCriterion:list[int]
    minLevel:int
    minSuccess:int
    lastEditPlayerName:str
    lastEditDate:int
    minLevelFacultative:bool
    minSuccessFacultative:bool
    invalidatedByModeration:bool
    recruitmentAutoLocked:bool
    
    
