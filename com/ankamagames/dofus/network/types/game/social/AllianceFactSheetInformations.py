from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


@dataclass
class AllianceFactSheetInformations(AllianceInformations):
    creationDate:int
    
    
    def __post_init__(self):
        super().__init__()
    