from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    protocolId = 8142
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    
    
