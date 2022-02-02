from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage


@dataclass
class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
    skillId:int
    
    
    def __post_init__(self):
        super().__init__()
    