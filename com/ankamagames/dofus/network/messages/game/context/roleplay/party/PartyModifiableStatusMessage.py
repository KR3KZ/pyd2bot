from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


@dataclass
class PartyModifiableStatusMessage(AbstractPartyMessage):
    enabled:bool
    
    
    def __post_init__(self):
        super().__init__()
    