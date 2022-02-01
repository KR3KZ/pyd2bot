from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(NetworkMessage):
    dungeonIds:list[int]
    
    
