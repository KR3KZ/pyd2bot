from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage


@dataclass
class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
    magicPoolStatus:int
    
    
    def __post_init__(self):
        super().__init__()
    