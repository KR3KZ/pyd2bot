from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


@dataclass
class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
    fightMap:MapCoordinatesExtended
    
    
    def __post_init__(self):
        super().__init__()
    