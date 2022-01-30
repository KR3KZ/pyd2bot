from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderListenRequestMessage(NetworkMessage):
    protocolId = 1266
    dungeonId:int
    
