from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


@dataclass
class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
    sellType:int
    options:list[HumanOption]
    
    
    def __post_init__(self):
        super().__init__()
    