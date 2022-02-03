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
    

    def init(self, applyText:str, guildId:int, timeSpent:int, filterLanguage:str, filterAmbiance:str, filterPlaytime:str, filterInterest:str, filterMinMaxGuildLevel:str, filterRecruitmentType:str, filterMinMaxCharacterLevel:str, filterMinMaxAchievement:str, filterSearchName:str, filterLastSort:str):
        self.applyText = applyText
        self.guildId = guildId
        self.timeSpent = timeSpent
        self.filterLanguage = filterLanguage
        self.filterAmbiance = filterAmbiance
        self.filterPlaytime = filterPlaytime
        self.filterInterest = filterInterest
        self.filterMinMaxGuildLevel = filterMinMaxGuildLevel
        self.filterRecruitmentType = filterRecruitmentType
        self.filterMinMaxCharacterLevel = filterMinMaxCharacterLevel
        self.filterMinMaxAchievement = filterMinMaxAchievement
        self.filterSearchName = filterSearchName
        self.filterLastSort = filterLastSort
        
        super().__init__()
    
    