from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntFlagRequestMessage(INetworkMessage):
    protocolId = 9576
    questType:int
    index:int
    
    
