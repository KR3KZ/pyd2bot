from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeWeightMessage(INetworkMessage):
    protocolId = 5653
    currentWeight:int
    maxWeight:int
    
    
