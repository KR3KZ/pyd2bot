from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(INetworkMessage):
    protocolId = 8522
    objectType:int
    typeDescription:int
    
    
