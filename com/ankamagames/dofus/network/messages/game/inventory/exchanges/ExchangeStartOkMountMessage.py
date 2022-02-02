from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


@dataclass
class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
    paddockedMountsDescription:list[MountClientData]
    
    
    def __post_init__(self):
        super().__init__()
    