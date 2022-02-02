from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


@dataclass
class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    target:int
    skillId:int
    
    
    def __post_init__(self):
        super().__init__()
    