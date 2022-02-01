from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations


class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    nbWaves:int
    alternatives:list[GroupMonsterStaticInformations]
    
    
