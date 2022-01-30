from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    protocolId = 8142
    kamas:float
    experience:float
    pods:int
    itemsValue:float
    
