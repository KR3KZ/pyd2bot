from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
    identification:'TaxCollectorStaticInformations'
    guildLevel:int
    taxCollectorAttack:int
    

    def init(self, identification:'TaxCollectorStaticInformations', guildLevel:int, taxCollectorAttack:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.identification = identification
        self.guildLevel = guildLevel
        self.taxCollectorAttack = taxCollectorAttack
        
        super().__init__(look, contextualId, disposition)
    
    