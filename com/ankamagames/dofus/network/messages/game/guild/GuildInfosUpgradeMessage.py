from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildInfosUpgradeMessage(INetworkMessage):
    protocolId = 2887
    maxTaxCollectorsCount:int
    taxCollectorsCount:int
    taxCollectorLifePoints:int
    taxCollectorDamagesBonuses:int
    taxCollectorPods:int
    taxCollectorProspecting:int
    taxCollectorWisdom:int
    boostPoints:int
    spellId:int
    spellLevel:int
    
    
