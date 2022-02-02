from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


@dataclass
class HumanOptionAlliance(HumanOption):
    allianceInformations:AllianceInformations
    aggressable:int
    
    
    def __post_init__(self):
        super().__init__()
    