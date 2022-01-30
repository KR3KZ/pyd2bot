from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(NetworkMessage):
    protocolId = 2640
    dungeonIds:list[int]
    
