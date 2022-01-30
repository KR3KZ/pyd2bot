from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderListenErrorMessage(NetworkMessage):
    protocolId = 7331
    dungeonId:int
    
