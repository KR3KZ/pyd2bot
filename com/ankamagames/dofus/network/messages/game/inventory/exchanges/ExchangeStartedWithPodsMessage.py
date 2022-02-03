from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    firstCharacterId:int
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:int
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    

    def init(self, firstCharacterId:int, firstCharacterCurrentWeight:int, firstCharacterMaxWeight:int, secondCharacterId:int, secondCharacterCurrentWeight:int, secondCharacterMaxWeight:int, exchangeType:int):
        self.firstCharacterId = firstCharacterId
        self.firstCharacterCurrentWeight = firstCharacterCurrentWeight
        self.firstCharacterMaxWeight = firstCharacterMaxWeight
        self.secondCharacterId = secondCharacterId
        self.secondCharacterCurrentWeight = secondCharacterCurrentWeight
        self.secondCharacterMaxWeight = secondCharacterMaxWeight
        
        super().__init__(exchangeType)
    
    