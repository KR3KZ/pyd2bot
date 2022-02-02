from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberGeoPosition import PartyMemberGeoPosition


@dataclass
class PartyLocateMembersMessage(AbstractPartyMessage):
    geopositions:list[PartyMemberGeoPosition]
    
    
    def __post_init__(self):
        super().__init__()
    