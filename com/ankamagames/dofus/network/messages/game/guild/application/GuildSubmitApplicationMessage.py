from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
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
    
    
    def __post_init__(self):
        super().__init__()
    