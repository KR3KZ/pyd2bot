from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildSubmitApplicationMessage(INetworkMessage):
    protocolId = 9276
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
    
    
