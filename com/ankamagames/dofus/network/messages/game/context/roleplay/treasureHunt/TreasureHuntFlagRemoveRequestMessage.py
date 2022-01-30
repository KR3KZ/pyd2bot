from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRemoveRequestMessage(NetworkMessage):
    protocolId = 6823
    questType:int
    index:int
    
