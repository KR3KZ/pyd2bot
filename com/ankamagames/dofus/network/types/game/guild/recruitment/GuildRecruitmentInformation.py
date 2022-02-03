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
    

    def init(self, guildId:int, recruitmentType:int, recruitmentTitle:str, recruitmentText:str, selectedLanguages:list[int], selectedCriterion:list[int], minLevel:int, minSuccess:int, lastEditPlayerName:str, lastEditDate:int):
        self.guildId = guildId
        self.recruitmentType = recruitmentType
        self.recruitmentTitle = recruitmentTitle
        self.recruitmentText = recruitmentText
        self.selectedLanguages = selectedLanguages
        self.selectedCriterion = selectedCriterion
        self.minLevel = minLevel
        self.minSuccess = minSuccess
        self.lastEditPlayerName = lastEditPlayerName
        self.lastEditDate = lastEditDate
        
        super().__init__()
    
    