from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntFinishedMessage(INetworkMessage):
    protocolId = 5016
    questType:int
    
    
