from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestAnswerMessage(NetworkMessage):
    protocolId = 8845
    questType:int
    result:int
    
    
