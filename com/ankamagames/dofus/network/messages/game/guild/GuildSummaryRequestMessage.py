from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


@dataclass
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
    
    
    def __post_init__(self):
        super().__init__()
    