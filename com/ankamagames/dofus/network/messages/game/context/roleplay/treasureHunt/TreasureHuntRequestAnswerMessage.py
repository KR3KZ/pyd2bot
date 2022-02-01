from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntRequestAnswerMessage(INetworkMessage):
    protocolId = 1019
    questType:int
    result:int
    
    
