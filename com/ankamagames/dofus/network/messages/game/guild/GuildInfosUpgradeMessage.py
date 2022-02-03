from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInfosUpgradeMessage(NetworkMessage):
    maxTaxCollectorsCount:int
    taxCollectorsCount:int
    taxCollectorLifePoints:int
    taxCollectorDamagesBonuses:int
    taxCollectorPods:int
    taxCollectorProspecting:int
    taxCollectorWisdom:int
    boostPoints:int
    spellId:list[int]
    spellLevel:list[int]
    

    def init(self, maxTaxCollectorsCount:int, taxCollectorsCount:int, taxCollectorLifePoints:int, taxCollectorDamagesBonuses:int, taxCollectorPods:int, taxCollectorProspecting:int, taxCollectorWisdom:int, boostPoints:int, spellId:list[int], spellLevel:list[int]):
        self.maxTaxCollectorsCount = maxTaxCollectorsCount
        self.taxCollectorsCount = taxCollectorsCount
        self.taxCollectorLifePoints = taxCollectorLifePoints
        self.taxCollectorDamagesBonuses = taxCollectorDamagesBonuses
        self.taxCollectorPods = taxCollectorPods
        self.taxCollectorProspecting = taxCollectorProspecting
        self.taxCollectorWisdom = taxCollectorWisdom
        self.boostPoints = boostPoints
        self.spellId = spellId
        self.spellLevel = spellLevel
        
        super().__init__()
    
    