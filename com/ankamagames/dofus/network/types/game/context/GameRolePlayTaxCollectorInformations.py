from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations


class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
    identification:TaxCollectorStaticInformations
    guildLevel:int
    taxCollectorAttack:int
    
    
