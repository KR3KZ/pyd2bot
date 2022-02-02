from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
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
    
    
    def __post_init__(self):
        super().__init__()
    