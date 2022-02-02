from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations


@dataclass
class PartyUpdateMessage(AbstractPartyEventMessage):
    memberInformations:PartyMemberInformations
    
    
    def __post_init__(self):
        super().__init__()
    