from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations


@dataclass
class PartyNewGuestMessage(AbstractPartyEventMessage):
    guest:PartyGuestInformations
    
    
    def __post_init__(self):
        super().__init__()
    