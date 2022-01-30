from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestAnswerMessage(NetworkMessage):
    protocolId = 8784
    questType:int
    result:int
    index:int
    
    
