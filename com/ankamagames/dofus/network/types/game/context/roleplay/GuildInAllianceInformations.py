from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class GuildInAllianceInformations(GuildInformations):
    nbMembers:int
    joinDate:int
    
    
    def __post_init__(self):
        super().__init__()
    