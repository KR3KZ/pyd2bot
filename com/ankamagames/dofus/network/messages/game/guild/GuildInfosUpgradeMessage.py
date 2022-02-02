from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
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
    
    
    def __post_init__(self):
        super().__init__()
    