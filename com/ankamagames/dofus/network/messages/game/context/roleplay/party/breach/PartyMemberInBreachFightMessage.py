from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


@dataclass
class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    floor:int
    room:int
    
    
    def __post_init__(self):
        super().__init__()
    