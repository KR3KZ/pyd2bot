from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


@dataclass
class PartyEntityMemberInformation(PartyEntityBaseInformation):
    initiative:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    
    
    def __post_init__(self):
        super().__init__()
    