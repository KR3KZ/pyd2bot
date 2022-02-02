from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListAddedMessage import ExchangeBidHouseInListAddedMessage


@dataclass
class ExchangeBidHouseInListUpdatedMessage(ExchangeBidHouseInListAddedMessage):
    
    
    def __post_init__(self):
        super().__init__()
    