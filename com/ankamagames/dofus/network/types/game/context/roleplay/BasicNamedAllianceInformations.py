from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


@dataclass
class BasicNamedAllianceInformations(BasicAllianceInformations):
    allianceName:str
    
    
    def __post_init__(self):
        super().__init__()
    