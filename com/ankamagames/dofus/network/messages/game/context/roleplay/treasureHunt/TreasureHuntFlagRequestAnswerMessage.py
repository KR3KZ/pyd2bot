from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestAnswerMessage(NetworkMessage):
    questType:int
    result:int
    index:int
    
    
