from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntGiveUpRequestMessage(INetworkMessage):
    protocolId = 2962
    questType:int
    
    
