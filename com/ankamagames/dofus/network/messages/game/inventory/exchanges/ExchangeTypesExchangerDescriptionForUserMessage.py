from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    typeDescription:list[int]
    

    def init(self, objectType:int, typeDescription:list[int]):
        self.objectType = objectType
        self.typeDescription = typeDescription
        
        super().__init__()
    
    