from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations


@dataclass
class GameFightMonsterInformations(GameFightAIInformations):
    creatureGenericId:int
    creatureGrade:int
    creatureLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    