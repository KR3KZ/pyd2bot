from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    protocolId = 2123
    firstCharacterId:float
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:float
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    
