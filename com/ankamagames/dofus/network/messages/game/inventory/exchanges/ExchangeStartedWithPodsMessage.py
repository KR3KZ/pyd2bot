from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    firstCharacterId:int
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:int
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    
    
