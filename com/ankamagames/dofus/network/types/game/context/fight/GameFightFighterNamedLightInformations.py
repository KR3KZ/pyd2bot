from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


@dataclass
class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
    name:str
    
    
    def __post_init__(self):
        super().__init__()
    