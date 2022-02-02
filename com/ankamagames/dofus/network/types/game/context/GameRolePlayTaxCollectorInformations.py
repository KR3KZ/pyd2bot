from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations


@dataclass
class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
    identification:TaxCollectorStaticInformations
    guildLevel:int
    taxCollectorAttack:int
    
    
    def __post_init__(self):
        super().__init__()
    