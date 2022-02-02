from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


@dataclass
class GameFightAIInformations(GameFightFighterInformations):
    
    
    def __post_init__(self):
        super().__init__()
    