from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations


class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
    protocolId = 3148
    staticInfos:GroupMonsterStaticInformations
    lootShare:int
    alignmentSide:int
    keyRingBonus:bool
    hasHardcoreDrop:bool
    hasAVARewardToken:bool
    
    
