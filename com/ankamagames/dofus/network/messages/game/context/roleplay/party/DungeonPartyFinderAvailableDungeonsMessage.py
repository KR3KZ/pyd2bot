from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderAvailableDungeonsMessage(INetworkMessage):
    protocolId = 2640
    dungeonIds:int
    
    
