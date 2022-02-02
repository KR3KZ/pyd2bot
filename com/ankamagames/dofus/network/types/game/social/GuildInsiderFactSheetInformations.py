from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations


@dataclass
class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
    leaderName:str
    nbConnectedMembers:int
    nbTaxCollectors:int
    
    
    def __post_init__(self):
        super().__init__()
    