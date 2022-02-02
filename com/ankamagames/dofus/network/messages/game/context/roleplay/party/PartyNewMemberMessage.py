from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateMessage import PartyUpdateMessage


@dataclass
class PartyNewMemberMessage(PartyUpdateMessage):
    
    
    def __post_init__(self):
        super().__init__()
    