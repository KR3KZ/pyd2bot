from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


@dataclass
class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    reason:int
    memberId:int
    memberAccountId:int
    memberName:str
    fightId:int
    timeBeforeFightStart:int
    
    
    def __post_init__(self):
        super().__init__()
    