from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import PartyMemberRemoveMessage


@dataclass
class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
    kickerId:int
    
    
    def __post_init__(self):
        super().__init__()
    