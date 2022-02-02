from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


@dataclass
class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    firstCharacterId:int
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:int
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    
    
    def __post_init__(self):
        super().__init__()
    