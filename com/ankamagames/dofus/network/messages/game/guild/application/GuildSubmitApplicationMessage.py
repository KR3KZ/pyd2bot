from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildSubmitApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    timeSpent:int
    filterLanguage:str
    filterAmbiance:str
    filterPlaytime:str
    filterInterest:str
    filterMinMaxGuildLevel:str
    filterRecruitmentType:str
    filterMinMaxCharacterLevel:str
    filterMinMaxAchievement:str
    filterSearchName:str
    filterLastSort:str
    
    
