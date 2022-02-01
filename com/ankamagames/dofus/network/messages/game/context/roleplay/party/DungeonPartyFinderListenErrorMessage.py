from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonPartyFinderListenErrorMessage(INetworkMessage):
    protocolId = 7331
    dungeonId:int
    
    
