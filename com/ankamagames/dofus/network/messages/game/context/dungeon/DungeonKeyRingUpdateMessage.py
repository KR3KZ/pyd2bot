from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonKeyRingUpdateMessage(NetworkMessage):
    protocolId = 2874
    dungeonId:int
    available:bool
    
