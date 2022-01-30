from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


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
    
    