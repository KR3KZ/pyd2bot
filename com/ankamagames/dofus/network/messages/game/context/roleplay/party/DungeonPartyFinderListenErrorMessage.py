from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderListenErrorMessage(INetworkMessage):
    protocolId = 7331
    dungeonId:int
    
    
