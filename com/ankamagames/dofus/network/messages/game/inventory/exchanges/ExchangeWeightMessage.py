from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeWeightMessage(NetworkMessage):
    protocolId = 5653
    currentWeight:int
    maxWeight:int
    
    
