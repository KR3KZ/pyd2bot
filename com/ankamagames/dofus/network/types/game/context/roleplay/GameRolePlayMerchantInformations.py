from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
    protocolId = 3425
    sellType:int
    options:HumanOption
    
    
