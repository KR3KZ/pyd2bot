from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class GuildSummaryRequestMessage(PaginationRequestAbstractMessage):
    protocolId = 9211
    nameFilter:str
    criterionFilter:int
    languagesFilter:int
    recruitmentTypeFilter:int
    minLevelFilter:int
    maxLevelFilter:int
    minPlayerLevelFilter:int
    maxPlayerLevelFilter:int
    minSuccessFilter:int
    maxSuccessFilter:int
    sortType:int
    hideFullFilter:bool
    sortDescending:bool
    
    
