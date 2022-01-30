from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations


class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
    protocolId = 345
    humanoidInfo:HumanInformations
    accountId:int
    
    
