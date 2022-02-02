from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage


@dataclass
class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
    enabled:bool
    
    
    def __post_init__(self):
        super().__init__()
    