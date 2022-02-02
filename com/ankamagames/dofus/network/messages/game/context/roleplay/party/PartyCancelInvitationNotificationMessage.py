from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


@dataclass
class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    cancelerId:int
    guestId:int
    
    
    def __post_init__(self):
        super().__init__()
    