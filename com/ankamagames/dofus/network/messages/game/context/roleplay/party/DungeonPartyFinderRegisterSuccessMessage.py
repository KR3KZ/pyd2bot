from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterSuccessMessage(NetworkMessage):
    protocolId = 2385
    dungeonIds:list[int]
    
