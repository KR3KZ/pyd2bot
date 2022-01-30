from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(INetworkMessage):
    protocolId = 3514
    skillId:int
    crafterJobLevel:int
    
    
