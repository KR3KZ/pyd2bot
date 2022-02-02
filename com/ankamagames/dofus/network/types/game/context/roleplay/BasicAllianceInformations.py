from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


@dataclass
class BasicAllianceInformations(AbstractSocialGroupInfos):
    allianceId:int
    allianceTag:str
    
    
    def __post_init__(self):
        super().__init__()
    