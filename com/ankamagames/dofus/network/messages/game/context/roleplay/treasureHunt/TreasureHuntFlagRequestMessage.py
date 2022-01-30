from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestMessage(NetworkMessage):
    protocolId = 9576
    questType:int
    index:int
    
    
