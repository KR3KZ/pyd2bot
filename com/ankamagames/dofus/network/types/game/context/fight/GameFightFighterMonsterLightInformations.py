from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


@dataclass
class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
    creatureGenericId:int
    
    
    def __post_init__(self):
        super().__init__()
    