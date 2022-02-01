from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntFlagRequestAnswerMessage(INetworkMessage):
    protocolId = 8784
    questType:int
    result:int
    index:int
    
    
