from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    protocolId = 6497
    availables:int
    unavailables:int
    
    
