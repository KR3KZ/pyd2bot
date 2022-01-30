from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations


class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    protocolId = 5382
    nbWaves:int
    alternatives:GroupMonsterStaticInformations
    
