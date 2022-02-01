from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(INetworkMessage):
    protocolId = 3514
    skillId:int
    crafterJobLevel:int
    
    
