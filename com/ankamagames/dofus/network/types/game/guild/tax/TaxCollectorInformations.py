from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorInformations(NetworkMessage):
    uniqueId:int
    firtNameId:int
    lastNameId:int
    additionalInfos:AdditionalTaxCollectorInformations
    worldX:int
    worldY:int
    subAreaId:int
    state:int
    look:EntityLook
    complements:list[TaxCollectorComplementaryInformations]
    
    
