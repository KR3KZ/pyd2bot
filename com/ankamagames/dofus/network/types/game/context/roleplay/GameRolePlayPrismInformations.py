from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation


@dataclass
class GameRolePlayPrismInformations(GameRolePlayActorInformations):
    prism:PrismInformation
    
    
    def __post_init__(self):
        super().__init__()
    