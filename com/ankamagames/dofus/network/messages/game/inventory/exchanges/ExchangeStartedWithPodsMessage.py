from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    protocolId = 2123
    firstCharacterId:int
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:int
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    
    
