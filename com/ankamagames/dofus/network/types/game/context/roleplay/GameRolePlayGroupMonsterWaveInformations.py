from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations


@dataclass
class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    nbWaves:int
    alternatives:list[GroupMonsterStaticInformations]
    
    
    def __post_init__(self):
        super().__init__()
    