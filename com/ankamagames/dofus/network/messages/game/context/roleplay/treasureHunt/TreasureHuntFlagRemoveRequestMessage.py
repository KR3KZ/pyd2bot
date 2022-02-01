from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntFlagRemoveRequestMessage(INetworkMessage):
    protocolId = 6823
    questType:int
    index:int
    
    
