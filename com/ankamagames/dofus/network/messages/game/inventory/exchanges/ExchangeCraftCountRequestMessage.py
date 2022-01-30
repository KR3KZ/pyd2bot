from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeCraftCountRequestMessage(INetworkMessage):
    protocolId = 7316
    count:int
    
    
