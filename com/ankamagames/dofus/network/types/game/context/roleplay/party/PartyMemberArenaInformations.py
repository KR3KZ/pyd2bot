from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations


@dataclass
class PartyMemberArenaInformations(PartyMemberInformations):
    rank:int
    
    
    def __post_init__(self):
        super().__init__()
    