from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(INetworkMessage):
    protocolId = 8522
    objectType:int
    typeDescription:int
    
    
