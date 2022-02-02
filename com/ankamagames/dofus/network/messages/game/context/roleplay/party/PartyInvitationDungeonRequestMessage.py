from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationRequestMessage import PartyInvitationRequestMessage


@dataclass
class PartyInvitationDungeonRequestMessage(PartyInvitationRequestMessage):
    dungeonId:int
    
    
    def __post_init__(self):
        super().__init__()
    