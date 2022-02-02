from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


@dataclass
class PartyInvitationMessage(AbstractPartyMessage):
    partyType:int
    partyName:str
    maxParticipants:int
    fromId:int
    fromName:str
    toId:int
    
    
    def __post_init__(self):
        super().__init__()
    