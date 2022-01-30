from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInfosUpgradeMessage(NetworkMessage):
    protocolId = 2887
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
    
