from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


@dataclass
class GameFightFighterEntityLightInformation(GameFightFighterLightInformations):
    entityModelId:int
    masterId:int
    
    
    def __post_init__(self):
        super().__init__()
    