from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
    


class TaxCollectorInformations(NetworkMessage):
    uniqueId:int
    firtNameId:int
    lastNameId:int
    additionalInfos:'AdditionalTaxCollectorInformations'
    worldX:int
    worldY:int
    subAreaId:int
    state:int
    look:'EntityLook'
    complements:list['TaxCollectorComplementaryInformations']
    

    def init(self, uniqueId:int, firtNameId:int, lastNameId:int, additionalInfos:'AdditionalTaxCollectorInformations', worldX:int, worldY:int, subAreaId:int, state:int, look:'EntityLook', complements:list['TaxCollectorComplementaryInformations']):
        self.uniqueId = uniqueId
        self.firtNameId = firtNameId
        self.lastNameId = lastNameId
        self.additionalInfos = additionalInfos
        self.worldX = worldX
        self.worldY = worldY
        self.subAreaId = subAreaId
        self.state = state
        self.look = look
        self.complements = complements
        
        super().__init__()
    
    