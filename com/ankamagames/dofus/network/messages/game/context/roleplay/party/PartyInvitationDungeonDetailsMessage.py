from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage


@dataclass
class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
    dungeonId:int
    playersDungeonReady:list[bool]
    
    
    def __post_init__(self):
        super().__init__()
    