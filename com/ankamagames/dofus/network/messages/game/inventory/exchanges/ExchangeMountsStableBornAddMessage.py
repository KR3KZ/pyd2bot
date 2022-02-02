from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsStableAddMessage import ExchangeMountsStableAddMessage


@dataclass
class ExchangeMountsStableBornAddMessage(ExchangeMountsStableAddMessage):
    
    
    def __post_init__(self):
        super().__init__()
    