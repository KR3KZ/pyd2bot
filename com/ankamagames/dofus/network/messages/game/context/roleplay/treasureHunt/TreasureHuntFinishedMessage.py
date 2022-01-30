from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFinishedMessage(NetworkMessage):
    protocolId = 5016
    questType:int
    
    
