from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations


@dataclass
class GameRolePlayMutantInformations(GameRolePlayHumanoidInformations):
    monsterId:int
    powerLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    