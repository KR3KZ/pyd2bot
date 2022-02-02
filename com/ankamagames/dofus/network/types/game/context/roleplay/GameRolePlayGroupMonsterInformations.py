from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations


@dataclass
class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
    staticInfos:GroupMonsterStaticInformations
    lootShare:int
    alignmentSide:int
    keyRingBonus:bool
    hasHardcoreDrop:bool
    hasAVARewardToken:bool
    
    
    def __post_init__(self):
        super().__init__()
    