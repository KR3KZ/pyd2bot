from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeReplyTaxVendorMessage(NetworkMessage):
    objectValue:int
    totalTaxValue:int
    
    
    def __post_init__(self):
        super().__init__()
    