from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterRequestMessage(NetworkMessage):
    protocolId = 2723
    dungeonIds:int
    
