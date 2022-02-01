from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntDigRequestAnswerMessage(INetworkMessage):
    protocolId = 8845
    questType:int
    result:int
    
    
