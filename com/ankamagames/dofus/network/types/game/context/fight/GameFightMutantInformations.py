from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations


@dataclass
class GameFightMutantInformations(GameFightFighterNamedInformations):
    powerLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    