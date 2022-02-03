from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    

    def init(self, kamas:int, experience:int, pods:int, itemsValue:int):
        self.kamas = kamas
        self.experience = experience
        self.pods = pods
        self.itemsValue = itemsValue
        
        super().__init__()
    
    