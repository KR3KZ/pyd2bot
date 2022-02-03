from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
    allianceIdentity:'AllianceInformations'
    

    def init(self, allianceIdentity:'AllianceInformations', firstNameId:int, lastNameId:int, guildIdentity:'GuildInformations', callerId:int):
        self.allianceIdentity = allianceIdentity
        
        super().__init__(firstNameId, lastNameId, guildIdentity, callerId)
    
    