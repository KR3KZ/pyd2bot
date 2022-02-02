from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


@dataclass
class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    followedId:int
    success:bool
    isFollowed:bool
    
    
    def __post_init__(self):
        super().__init__()
    