from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeWeightMessage(INetworkMessage):
    protocolId = 5653
    currentWeight:int
    maxWeight:int
    
    
