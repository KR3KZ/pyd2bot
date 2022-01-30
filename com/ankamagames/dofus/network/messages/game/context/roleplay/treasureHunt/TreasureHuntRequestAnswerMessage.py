from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntRequestAnswerMessage(NetworkMessage):
    protocolId = 1019
    questType:int
    result:int
    
    
