from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestMessage(NetworkMessage):
    protocolId = 6219
    questType:int
    
    
