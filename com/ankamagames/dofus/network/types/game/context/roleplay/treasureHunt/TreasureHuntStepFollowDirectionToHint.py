from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


@dataclass
class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
    direction:int
    npcId:int
    
    
    def __post_init__(self):
        super().__init__()
    