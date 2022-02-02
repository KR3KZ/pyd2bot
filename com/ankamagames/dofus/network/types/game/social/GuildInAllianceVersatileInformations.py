from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


@dataclass
class GuildInAllianceVersatileInformations(GuildVersatileInformations):
    allianceId:int
    
    
    def __post_init__(self):
        super().__init__()
    