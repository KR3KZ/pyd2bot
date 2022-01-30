from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderListenRequestMessage(INetworkMessage):
    protocolId = 1266
    dungeonId:int
    
    
