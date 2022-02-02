from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations


@dataclass
class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
    humanoidInfo:HumanInformations
    accountId:int
    
    
    def __post_init__(self):
        super().__init__()
    