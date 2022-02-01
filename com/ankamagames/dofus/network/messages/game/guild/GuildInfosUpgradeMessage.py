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
    
    
