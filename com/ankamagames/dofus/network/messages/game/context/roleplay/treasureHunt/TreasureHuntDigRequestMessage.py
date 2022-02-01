from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntDigRequestMessage(INetworkMessage):
    protocolId = 6219
    questType:int
    
    
