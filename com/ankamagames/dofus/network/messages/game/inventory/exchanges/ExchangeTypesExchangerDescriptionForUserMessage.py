from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    typeDescription:list[int]
    
    
