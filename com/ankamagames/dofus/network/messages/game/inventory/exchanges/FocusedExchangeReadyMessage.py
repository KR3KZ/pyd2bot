from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReadyMessage import ExchangeReadyMessage


@dataclass
class FocusedExchangeReadyMessage(ExchangeReadyMessage):
    focusActionId:int
    
    
    def __post_init__(self):
        super().__init__()
    