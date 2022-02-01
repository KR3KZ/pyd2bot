from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorInformations(INetworkMessage):
    protocolId = 3820
    uniqueId:int
    firtNameId:int
    lastNameId:int
    additionalInfos:AdditionalTaxCollectorInformations
    worldX:int
    worldY:int
    subAreaId:int
    state:int
    look:EntityLook
    complements:TaxCollectorComplementaryInformations
    
    
