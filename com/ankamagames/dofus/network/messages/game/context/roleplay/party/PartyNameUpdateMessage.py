from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


@dataclass
class PartyNameUpdateMessage(AbstractPartyMessage):
    partyName:str
    
    
    def __post_init__(self):
        super().__init__()
    