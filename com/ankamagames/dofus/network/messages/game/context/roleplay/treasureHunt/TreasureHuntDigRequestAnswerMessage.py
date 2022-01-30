from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntDigRequestAnswerMessage(INetworkMessage):
    protocolId = 8845
    questType:int
    result:int
    
    
