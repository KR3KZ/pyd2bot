from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateLightMessage import PartyUpdateLightMessage


@dataclass
class PartyEntityUpdateLightMessage(PartyUpdateLightMessage):
    indexId:int
    
    
    def __post_init__(self):
        super().__init__()
    