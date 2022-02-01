from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonPartyFinderListenRequestMessage(INetworkMessage):
    protocolId = 1266
    dungeonId:int
    
    
