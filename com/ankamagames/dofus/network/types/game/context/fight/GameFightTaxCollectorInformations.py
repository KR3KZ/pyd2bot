from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations


@dataclass
class GameFightTaxCollectorInformations(GameFightAIInformations):
    firstNameId:int
    lastNameId:int
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    