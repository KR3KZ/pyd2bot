from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


@dataclass
class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
    direction:int
    poiLabelId:int
    
    
    def __post_init__(self):
        super().__init__()
    