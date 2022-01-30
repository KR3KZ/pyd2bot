from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftCountRequestMessage(NetworkMessage):
    protocolId = 7316
    count:int
    
