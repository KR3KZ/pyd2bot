from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


@dataclass
class GameRolePlayTreasureHintInformations(GameRolePlayActorInformations):
    npcId:int
    
    
    def __post_init__(self):
        super().__init__()
    