from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


@dataclass
class TreasureHuntStepFollowDirection(TreasureHuntStep):
    direction:int
    mapCount:int
    
    
    def __post_init__(self):
        super().__init__()
    