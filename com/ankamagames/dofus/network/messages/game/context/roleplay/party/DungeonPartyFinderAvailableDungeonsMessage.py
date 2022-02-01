from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(INetworkMessage):
    protocolId = 2640
    dungeonIds:int
    
    
