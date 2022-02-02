from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import ExchangeObjectMovePricedMessage


@dataclass
class ExchangeObjectModifyPricedMessage(ExchangeObjectMovePricedMessage):
    
    
    def __post_init__(self):
        super().__init__()
    