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
    
    
