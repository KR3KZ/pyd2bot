from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.alliance.AllianceJoinedMessage import AllianceJoinedMessage


@dataclass
class AllianceMembershipMessage(AllianceJoinedMessage):
    
    
    def __post_init__(self):
        super().__init__()
    