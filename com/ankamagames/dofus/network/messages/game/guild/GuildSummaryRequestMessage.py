from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class GuildSummaryRequestMessage(PaginationRequestAbstractMessage):
    nameFilter:str
    criterionFilter:list[int]
    languagesFilter:list[int]
    recruitmentTypeFilter:list[int]
    minLevelFilter:int
    maxLevelFilter:int
    minPlayerLevelFilter:int
    maxPlayerLevelFilter:int
    minSuccessFilter:int
    maxSuccessFilter:int
    sortType:int
    hideFullFilter:bool
    sortDescending:bool
    

    def init(self, nameFilter:str, criterionFilter:list[int], languagesFilter:list[int], recruitmentTypeFilter:list[int], minLevelFilter:int, maxLevelFilter:int, minPlayerLevelFilter:int, maxPlayerLevelFilter:int, minSuccessFilter:int, maxSuccessFilter:int, sortType:int, offset:int, count:int):
        self.nameFilter = nameFilter
        self.criterionFilter = criterionFilter
        self.languagesFilter = languagesFilter
        self.recruitmentTypeFilter = recruitmentTypeFilter
        self.minLevelFilter = minLevelFilter
        self.maxLevelFilter = maxLevelFilter
        self.minPlayerLevelFilter = minPlayerLevelFilter
        self.maxPlayerLevelFilter = maxPlayerLevelFilter
        self.minSuccessFilter = minSuccessFilter
        self.maxSuccessFilter = maxSuccessFilter
        self.sortType = sortType
        
        super().__init__(offset, count)
    
    