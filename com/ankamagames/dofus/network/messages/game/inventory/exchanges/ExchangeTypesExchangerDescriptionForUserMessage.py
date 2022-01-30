from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(NetworkMessage):
    protocolId = 8522
    objectType:int
    typeDescription:int
    
    
