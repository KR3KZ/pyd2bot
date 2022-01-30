from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(NetworkMessage):
    protocolId = 3514
    skillId:int
    crafterJobLevel:int
    
