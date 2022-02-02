from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import PartyInvitationMessage


@dataclass
class PartyInvitationDungeonMessage(PartyInvitationMessage):
    dungeonId:int
    
    
    def __post_init__(self):
        super().__init__()
    