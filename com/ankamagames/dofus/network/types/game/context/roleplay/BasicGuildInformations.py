from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


@dataclass
class BasicGuildInformations(AbstractSocialGroupInfos):
    guildId:int
    guildName:str
    guildLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    